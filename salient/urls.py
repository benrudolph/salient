from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'salient.views.home', name='home'),
    url(r'^analyzer/', include('analyzer.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^uploader/', include('uploader.urls')),
    url(r'^$', include('visualize.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
