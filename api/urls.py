from django.conf.urls import patterns

from .views import DocAPIView, DocDetailAPIView, VolumeAPIView, VolumeDetailAPIView

urlpatterns = patterns('',
    (r'^docs/$', DocAPIView.as_view()),
    (r'^docs/(?P<pk>[0-9]+)/$', DocDetailAPIView.as_view()),
    (r'^volumes/$', VolumeAPIView.as_view()),
    (r'^volumes/(?P<pk>[0-9]+)/$', VolumeDetailAPIView.as_view()),
)
