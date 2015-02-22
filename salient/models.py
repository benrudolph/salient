from hashlib import sha224

from django.db import models
from django.contrib.auth.models import User


class Volume(models.Model):
  name = models.CharField(max_length=200)
  user = models.ForeignKey(User)

  def __str__(self):
    return self.name

class Doc(models.Model):
  name = models.CharField(max_length=200)
  volumes = models.ManyToManyField(Volume, blank=True)
  user = models.ForeignKey(User)

  URL = 'UR'
  TEXT = 'TX'
  INPUT = 'IN'

  DOC_TYPES = (
      (URL, 'Web Address'),
      (TEXT, 'Text Files'),
      (INPUT, 'User Input'),
  )

  doc_type = models.CharField(max_length=2,
                              choices=DOC_TYPES,
                              default=INPUT)

  # Used only when the doc is TEXT type
  text_file = models.FileField(upload_to='docs', null=True, blank=True)

  text = models.TextField(null=True, blank=True)

  text_hash = models.CharField(max_length=200, null=True, blank=True)

  url = models.CharField(max_length=1000, null=True, blank=True)

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    if self.text:
        self.text_hash = sha224(self.text.encode('utf-8')).hexdigest()
    super(Doc, self).save(*args, **kwargs)

class WordDoc(models.Model):
  doc = models.ForeignKey(Doc, null=True, blank=True)

  word_stemmed = models.CharField(max_length=100, null=True)
  word_raw = models.CharField(max_length=100, null=True)
  position = models.IntegerField(null=True)
  is_stopword = models.BooleanField(default=False, blank=True)
