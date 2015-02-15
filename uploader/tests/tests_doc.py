from django.test import TestCase
from hashlib import sha224

from accounts.models import User
from salient.models import Doc

class DocTest(TestCase):
    def setUp(self):
        self.user = User(username="ben", password="password")
        self.user.save()

        self.doc = Doc(
            name="test",
            user=self.user,
            text="A little text")
        self.doc.save()

    def test_text_hash(self):
        one = 'one'
        two = 'two'

        hash_one = sha224(one).hexdigest()
        hash_two = sha224(two).hexdigest()

        self.doc.text = one
        self.doc.save()

        self.assertEqual(self.doc.text_hash, hash_one)

        self.doc.text = two
        self.doc.save()

        self.assertEqual(self.doc.text_hash, hash_two)
