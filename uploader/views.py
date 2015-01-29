from django.shortcuts import render

def index(request):
  context = {}

  return render(request, 'uploader/index.html', context)
