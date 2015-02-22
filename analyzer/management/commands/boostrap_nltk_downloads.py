from django.core.management.base import BaseCommand, CommandError
import nltk

class Command(BaseCommand):
    help = 'Bootstraps application with nltk downloads'

    def handle(self, *args, **options):
        downloads = [
                'stopwords',
                'movie_reviews',
                'punkt',
                ]

        nltk.download(downloads)
