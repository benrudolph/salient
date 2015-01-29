from django.conf.urls import patterns, url, include

from uploader import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)



