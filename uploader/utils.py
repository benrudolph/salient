from django.db import models
from django.core.cache import cache
from django.db.models.loading import cache as app_cache
from django.db import transaction, connection
from django.db.models.signals import class_prepared
from django.db import models, migrations

import logging
logger = logging.getLogger('uploader')


def get_cached_model(app_label, model_name, regenerate=False, get_local_hash=lambda i: i._hash):

    # If this model has already been generated, we'll find it here
    try:
        previous_model = models.get_model(app_label, model_name)
    except LookupError:
        previous_model = None

    # We can force regeneration by disregarding the previous model
    if regenerate:
        previous_model = None
        # Django keeps a cache of registered models, we need to make room for
        # our new one
        utils.remove_from_model_cache(app_label, model_name)

    return previous_model


def remove_from_model_cache(app_label, model_name):
    """ Removes the given model from the model cache. """
    try:
        del app_cache.app_models[app_label][model_name.lower()]
    except KeyError:
        pass

def notify_model_change(model):
    """ Notifies other processes that a dynamic model has changed.
        This should only ever be called after the required database changes have been made.
    """
    CACHE_KEY = HASH_CACHE_TEMPLATE % (model._meta.app_label, model._meta.object_name)
    cache.set(CACHE_KEY, model._hash)
    logger.debug("Setting \"%s\" hash to: %s" % (model._meta.verbose_name, model._hash))


def _get_fields(model_class):
    """ Return a list of fields that require table columns. """
    return [(f.name, f) for f in model_class._meta.local_fields]


@transaction.atomic
def add_necessary_db_columns(model_class):
    """ Creates new table or relevant columns as necessary based on the model_class.
        No columns or data are renamed or removed.
        This is available in case a database exception occurs.
    """

    # Create table if missing
    create_db_table(model_class)

    # Add field columns if missing
    table_name = model_class._meta.db_table
    table_description = connection.introspection.get_table_description(
        connection.cursor(), table_name)

    fields = _get_fields(model_class)
    db_column_names = [row[0] for row in table_description]

    for field_name, field in fields:
        if field.column not in db_column_names:
            logger.debug("[SOMETHING IS WRONG] Adding field '%s' to table '%s'" % (field_name, table_name))


            # db.add_column(table_name, field_name, field)


    # Some columns require deferred SQL to be run. This was collected
    # when running db.add_column().
    # db.execute_deferred_sql()

def when_classes_prepared(app_name, dependencies, fn):
    """ Runs the given function as soon as the model dependencies are available.
        You can use this to build dyanmic model classes on startup instead of
        runtime.
        app_name       the name of the relevant app
        dependencies   a list of model names that need to have already been
                       prepared before the dynamic classes can be built.
        fn             this will be called as soon as the all required models
                       have been prepared
        NB: The fn will be called as soon as the last required
            model has been prepared. This can happen in the middle of reading
            your models.py file, before potentially referenced functions have
            been loaded. Becaue this function must be called before any
            relevant model is defined, the only workaround is currently to
            move the required functions before the dependencies are declared.
        TODO: Allow dependencies from other apps?
    """
    dependencies = [x.lower() for x in dependencies]

    def _class_prepared_handler(sender, **kwargs):
        """ Signal handler for class_prepared.
            This will be run for every model, looking for the moment when all
            dependent models are prepared for the first time. It will then run
            the given function, only once.
        """
        sender_name = sender._meta.object_name.lower()
        already_prepared = set(app_cache.all_models.get(app_name,{}).keys() + [sender_name])

        if (sender._meta.app_label == app_name and sender_name in dependencies
          and all([x in already_prepared for x in dependencies])):
            with transaction.atomic():
                fn()

    # Connect the above handler to the class_prepared signal
    # NB: Although this signal is officially documented, the documentation
    # notes the following:
    #     "Django uses this signal internally; it's not generally used in
    #      third-party applications."
    class_prepared.connect(_class_prepared_handler, weak=False)


@transaction.atomic
def create_db_table(model_class):
    """ Takes a Django model class and create a database table, if necessary.
    """
    # XXX Create related tables for ManyToMany etc

    table_name = model_class._meta.db_table
    class_name = model_class.__name__

    # Introspect the database to see if it doesn't already exist
    if (connection.introspection.table_name_converter(table_name)
                        not in connection.introspection.table_names()):

        install(model_class)
        logger.debug("Created table '%s'" % table_name)

def install(model):
    from django.core.management import sql, color

    # Standard syncdb expects models to be in reliable locations,
    # so dynamic models need to bypass django.core.management.syncdb.
    # On the plus side, this allows individual models to be installed
    # without installing the entire project structure.
    # On the other hand, this means that things like relationships and
    # indexes will have to be handled manually.
    # This installs only the basic table definition.

    # disable terminal colors in the sql statements
    s = color.no_style()

    cursor = connection.cursor()
    statements, pending = connection.creation.sql_create_model(model, s)
    for sql in statements:
        cursor.execute(sql)


HASH_CACHE_TEMPLATE = 'dynamic_model_hash_%s-%s'
