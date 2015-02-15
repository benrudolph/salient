from django.conf.urls import patterns

from .views import DocAPIView, DocDetailAPIView, VolumeAPIView

urlpatterns = patterns('',
    (r'^docs/$', DocAPIView.as_view()),
    (r'^docs/(?P<pk>[0-9]+)/$', DocDetailAPIView.as_view()),
    (r'^volumes/$', VolumeAPIView.as_view()),
)
