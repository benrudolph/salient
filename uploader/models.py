from django.db import models
from django.contrib.auth.models import User

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

