from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class SalientUser(models.Model):
  user = models.OneToOneField(User)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        SalientUser.objects.get_or_create(user=kwargs.get('instance'))
