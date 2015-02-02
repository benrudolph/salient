from django.shortcuts import render
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

class VolumeCreateView(CreateView):
  form_class = VolumeForm
  template_name = 'uploader/volume/create_form.html'
  success_url = '/uploader/'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    self.object.doc_set = form.cleaned_data['docs']
    form.save_m2m()

    return super(ModelFormMixin, self).form_valid(form)

class VolumeListView(ListView):
  template_name = 'uploader/volume/list.html'
  model = Volume

class VolumeUpdateView(UpdateView):
  template_name = 'uploader/volume/update.html'
  success_url = '/uploader/'
  model = Volume
  form_class = VolumeUpdateForm

class DocCreateView(CreateView):
  form_class = DocForm
  template_name = 'uploader/doc/create_form.html'
  success_url = '/uploader/'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    form.save_m2m()

    return super(ModelFormMixin, self).form_valid(form)
