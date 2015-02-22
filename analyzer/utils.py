import re
import pickle

from nltk import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.util import ngrams

IS_WORD = re.compile('\w+')

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
            'position': i,
            'is_stopword': not IS_WORD.search(token) or
                           token in stopwords.words('english')
            })



    return result

def stem_word(word):
    return PorterStemmer().stem(word)

def compute_sentiment(text):
    tokens = word_tokenize(text)

    with open('classifiers/movie_reviews_sklearn.LogisticRegression.pickle') as pk:
        classifier = pickle.load(pk)

        # Features for unigram and bigrams
        feats = dict([(token, True) for token in tokens])
        feats.update(dict([(bigram, True) for bigram in ngrams(tokens, 2)]))

        dist = classifier.prob_classify(feats)
        return { 'neg': dist.prob('neg'), 'pos': dist.prob('pos') }

    return None
