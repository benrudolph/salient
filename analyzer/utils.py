from django.core.cache import cache

def parse(text):
    """Returns a list of dictionaries. Each dictionary contains:

    {
        word_stemmed: <stemmed word>
        word_raw: <raw word>
        position: <position word was found>
    }
    """
    pass
