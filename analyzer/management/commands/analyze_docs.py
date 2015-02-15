from django.core.management.base import BaseCommand, CommandError
from salient.models import Doc
from analyzer.tasks import parse_doc

class Command(BaseCommand):
    help = 'Analyzes all documents in database'

    def handle(self, *args, **options):
        docs = Doc.objects.all()

        for doc in docs:
            doc.worddoc_set.all().delete()
            parse_doc(doc)
