from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from .forms import UserForm

def register(request):

  registered = False

  if request.method == 'POST':
    form = UserForm(data=request.POST)

    if form.is_valid():
      user = form.save()
      return HttpResponseRedirect('/')

    registered = True
  else:
    form = UserForm()

  context = {
      'user_form': form,
      'registered': registered
      }
  return render(request, 'registration/register.html', context)
