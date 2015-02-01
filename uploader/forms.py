from django import forms

from salient.forms import *
from crispy_forms.layout import Layout, Div

from .models import *

class VolumeForm(SalientModelForm):
  class Meta:
    model = Volume
    fields = ['name']

class DocForm(SalientModelForm):

  def __init__(self, *args, **kwargs):
    super(DocForm, self).__init__(*args, **kwargs)

    self.helper.layout = Layout(
        'name',
        'volume',
        'doc_type',
        Div(
            'url',
            data_bind='visible: showUrl'),
        Div(
            'text_file',
            data_bind='visible: showTextFile'),
        Div(
            'text',
            data_bind='visible: showInput'),
    )

  class Meta:
    model = Doc
    fields = ['name', 'volume', 'doc_type', 'text_file', 'text', 'url']
    doc_type_data_bind = """
        value: docType
        """
  
    widgets = {
      'doc_type': forms.Select(attrs={'data-bind': doc_type_data_bind}),
      'url': forms.TextInput(attrs={'data-bind': 'visible: showUrl'}),
      'text': forms.Textarea(attrs={'data-bind': 'visible: showInput'}),
      'text_file': forms.ClearableFileInput(attrs={'data-bind': 'visible: showTextFile'}),
    }
