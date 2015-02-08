from django.db import models
from . import utils

def get_word_doc_model(doc, regenerate=False, notify_changes=True):
    """ Takes a doc object and returns a model for the word model.
        Setting regenerate forces a regeneration, regardless of cached models.
        Setting notify_changes updates the cache with the current hash.
    """

    name = doc.name
    _app_label = 'uploader'
    _model_name = 'WordDoc{unique_id}'.format(unique_id=doc.id)

    # Skip regeneration if we have a valid cached model
    cached_model = utils.get_cached_model(_app_label, _model_name, regenerate)
    if cached_model is not None:
        return cached_model

     # Collect the dynamic model's class attributes
    attrs = {
        '__module__': __name__,
        '__unicode__': lambda s: '%s word doc' % name,
        'word_stemmed': models.CharField(max_length=100, null=True),
        'word_raw': models.CharField(max_length=100, null=True),
        'position': models.IntegerField(null=True),
        'doc_id': models.IntegerField(null=True),
        'volume_id': models.IntegerField(null=True),
    }

    class Meta:
        app_label = 'uploader'
        verbose_name = doc.name + ' Word Document'

    attrs['Meta'] = Meta

    # Add a hash representing this model to help quickly identify changes
    attrs['_hash'] = generate_model_hash(doc)

    model = type(_model_name, (models.Model,), attrs)

    # You could create the table and columns here if you're paranoid that it
    # hasn't happened yet.
    #utils.create_db_table(model)
    # Be wary though, that you won't be able to rename columns unless you
    # prevent the following line from being run.
    #utils.add_necessary_db_columns(model)

    if notify_changes:
        utils.notify_model_change(model)

    return model

def build_existing_word_doc_models():
    """ Builds all existing dynamic models at once. """
    # To avoid circular imports, the model is retrieved from the model cache
    Doc = models.get_model('uploader', 'Doc')
    for doc in Doc.objects.all():
        WordDoc = get_word_doc_model(doc)
        # Create the table if necessary, shouldn't be necessary anyway
        utils.create_db_table(WordDoc)
        # While we're at it...
        utils.add_necessary_db_columns(WordDoc)


def generate_model_hash(doc):
    return doc.get_hash_string()

