from django.conf.urls import url
from qa.views import test, get_main, get_question, get_popular, post_question, signup, login

urlpatterns = [
    url(r'^$', get_main, name='get_main'),
    url(r'^login/', login, name='login'),
    url(r'^signup/', signup, name='signup'),
    url(r'^question/(?P<qn>\d+)/', get_question, name='get_question'),
    url(r'^ask/', post_question, name='post_question'),
    url(r'^popular/', get_popular, name='get_popular'),
	url(r'^new/', test, name='test')
]