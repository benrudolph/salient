from . import utils

def doc_post_save(sender, instance, created, **kwargs):
    """ Ensure that a table exists for this logger. """

    # Force our response model to regenerate
    WordDoc = instance.get_word_doc_model(regenerate=True, notify_changes=False)

    # Create a new table if it's missing
    utils.create_db_table(WordDoc)

    # Tell other process to regenerate their models
    utils.notify_model_change(WordDoc)


def doc_pre_delete(sender, instance, **kwargs):
    WordDoc = instance.WordDoc

    # delete the data tables? (!)
    #utils.delete_db_table(Response)
