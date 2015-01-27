from django.conf.urls import patterns, url, include
from django.views.generic.edit import CreateView

from accounts import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^register/', views.register, name='register'),
)

