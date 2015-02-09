from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

def parse(text):
    """Returns a list of dictionaries. Each dictionary contains:

    {
        word_stemmed: <stemmed word>
        word_raw: <raw word>
        position: <position word was found>
    }
    """

    tokens = word_tokenize(text)
    stemmer = PorterStemmer()

    result = []

    for i, token in enumerate(tokens):
        result.append({
            'word_stemmed': stemmer.stem(token),
            'word_raw': token,
            'position': i
            })

    return result
