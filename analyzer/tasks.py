from __future__ import absolute_import

from salient.celery import app
from salient.models import WordDoc

from .utils import parse, compute_sentiment

@app.task
def parse_doc(doc):
    word_docs = parse(doc.text)

    for word_doc in word_docs:
        word_doc.update({ 'doc_id': doc.id })

    doc.worddoc_set.bulk_create(
            [WordDoc(**word_doc) for word_doc in word_docs]
            )

    sentiment = compute_sentiment(doc.text)

    if sentiment:
        doc.sentiment_neg = sentiment['neg']
        doc.sentiment_pos = sentiment['pos']
        doc.save()
