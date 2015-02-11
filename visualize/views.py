from django.shortcuts import render
from django.views.generic import TemplateView

class DocVisualizeView(TemplateView):
    template_name = 'visualize/doc_visualize.html'


