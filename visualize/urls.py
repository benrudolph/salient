from django.conf.urls import patterns

from .views import DocVisualizeView

urlpatterns = patterns('',
    (r'^$', DocVisualizeView.as_view()),
)

