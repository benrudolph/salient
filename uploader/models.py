from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete

from . import utils
from . import signals
from .dynamic_models import get_word_doc_model, build_existing_word_doc_models

class Volume(models.Model):
  name = models.CharField(max_length=200)
  user = models.ForeignKey(User)

  def __str__(self):
    return self.name

class Doc(models.Model):
  name = models.CharField(max_length=200)
  volumes = models.ManyToManyField(Volume, null=True, blank=True)
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

  url = models.CharField(max_length=1000, null=True, blank=True)

  def __str__(self):
    return self.name

  def get_hash_string(self):
    return self.id

  def get_word_doc_model(self, regenerate=False, notify_changes=True):
    return get_word_doc_model(self, regenerate=regenerate, notify_changes=notify_changes)


  @property
  def WordDoc(self):
    " Convenient access the relevant model class for the responses "
    return get_word_doc_model(self)

# Connect signals
post_save.connect(signals.doc_post_save, sender=Doc)
pre_delete.connect(signals.doc_pre_delete, sender=Doc)

# Build all existing word doc models as soon as possible
# This is optional, but is nice as it avoids building the model when the
# first relevant view is loaded.
utils.when_classes_prepared('uploader', ['Doc'],
                              build_existing_word_doc_models)
