import subprocess
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Bootstraps application with classifiers'

    def handle(self, *args, **options):
        algorithm = 'sklearn.LogisticRegression'
        corpus = 'movie_reviews'

        trainer_path = os.path.join(settings.BASE_DIR, 'submodules/nltk-trainer', 'train_classifier.py')
        classifier_path = os.path.join(settings.BASE_DIR,
                'classifiers',
                '{corpus}_{algorithm}.pickle'.format(corpus=corpus, algorithm=algorithm))

        # Movie Review LR classifier
        ret = subprocess.call([
            'python',
            trainer_path,
            corpus,
            '--instances', 'paras',
            '--filename', classifier_path,
            '--classifier', algorithm,
            '--fraction', '0.75',
            '--min_score', '2',
            '--ngrams', '1', '2',
            ])

        if ret:
            print 'Something went wrong!'
        else:
            print 'Successfully created movie review classifier!'
