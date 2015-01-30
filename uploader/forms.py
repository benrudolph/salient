from django import forms

from .models import *

class VolumeForm(forms.ModelForm):

  class Meta:
    model = Volume
    fields = ['name']

class DocForm(forms.ModelForm):

  class Meta:
    model = Doc
    fields = ['name', 'volume', 'doc_type', 'text_file', 'text', 'url']
