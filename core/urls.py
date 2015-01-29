from django.conf.urls import patterns, url, include

from core import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='register'),
)


