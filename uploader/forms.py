from django import forms

from salient.forms import *

from .models import *

class VolumeForm(SalientForm):

  class Meta:
    model = Volume
    fields = ['name']

class DocForm(SalientForm):

  class Meta:
    model = Doc
    fields = ['name', 'volume', 'doc_type', 'text_file', 'text', 'url']
