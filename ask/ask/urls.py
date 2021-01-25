
from django.conf.urls import include, url
from qa.views import test, get_main, get_popular

urlpatterns = [
    url(r'^$', test, name='test'),
    url(r'^login/$', test, name='test'),
    url(r'^signup/$', test, name='test'),
    url(r'^/$', get_main, name='get_main'),
    url(r'^question/.+', include('qa.urls')),
    url(r'^popular/$', get_popular, name='get_popular'),
    url(r'^ask/$', test, name='test'),
	url(r'^new/$', test, name='test')
]
