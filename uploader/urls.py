from django.conf.urls import patterns, url, include

from uploader import views

urlpatterns = patterns('',
    url(r'^$', views.VolumeListView.as_view(), name='volume_list'),
    url(r'^volume/create/$', views.VolumeCreateView.as_view(), name='volume_create'),
    url(r'^volume/update/(?P<pk>\d+)/$', views.VolumeUpdateView.as_view(), name='volume_update'),

    url(r'^doc/create/$', views.DocCreateView.as_view(), name='doc_create'),
    url(r'^doc/edit/(\d+)/$', views.DocCreateView.as_view(), name='doc_edit'),


)



