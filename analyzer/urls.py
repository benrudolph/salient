from django.conf.urls import patterns, url

from .views import DocWordFrequencyAPIView, DocWordXRayAPIView

urlpatterns = patterns('',
    (r'^docs/(?P<pk>[0-9]+)/word_frequency$', DocWordFrequencyAPIView.as_view()),
    (r'^docs/(?P<pk>[0-9]+)/xray$', DocWordXRayAPIView.as_view()),
)
