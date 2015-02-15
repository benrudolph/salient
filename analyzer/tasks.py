from __future__ import absolute_import

from salient.celery import app
from salient.models import WordDoc

from .utils import parse

@app.task
def parse_doc(doc):
    word_docs = parse(doc.text)

    WordDoc.objects.bulk_create(
            [WordDoc(**word_doc) for word_doc in word_docs]
            )

