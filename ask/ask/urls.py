
from django.urls import include,path
from qa.views import test

urlpatterns = [
    path(r'^$', test, name='test'),
    path(r'^login/$', test, name='test'),
    path(r'^signup/$', test, name='test'),
    path(r'^question/', include('qa.urls')),
    path(r'^ask/$', test, name='test'),
    path(r'^popular/$', test, name='test'),
	path(r'^new/$', test, name='test')
]
