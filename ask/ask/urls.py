
from django.conf.urls import include, url
from qa.views import test

urlpatterns = [
    url(r'^$', test, name='test'),
    url(r'^login/$', test, name='test'),
    url(r'^signup/$', test, name='test'),
    url(r'^question/.+', include('qa.urls')),
    url(r'^ask/$', test, name='test'),
    url(r'^popular/$', test, name='test'),
	url(r'^new/$', test, name='test')
]
