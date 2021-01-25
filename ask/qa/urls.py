from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^(?P<qn>\d+)/$', views.get_question)   
]