from django.db import models

class Doc(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Volume(models.Model):
  name = models.CharField(max_length=200)
  docs = models.ManyToManyField(Doc)


