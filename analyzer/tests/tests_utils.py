from django.test import TestCase

from analyzer import utils

class UtilsTest(TestCase):
    def setUp(self):
        self.text = """
        Here is a test text.
        It has a few sentences.
        And a couple of words.
        """

    def test_parse_basic(self):
        result = utils.parse(self.text)

        self.assertEqual(len(result), 18)

        for d in result:
            self.assertIsNotNone(d['word_stemmed'])
            self.assertIsNotNone(d['word_raw'])
            self.assertIsNotNone(d['position'])
