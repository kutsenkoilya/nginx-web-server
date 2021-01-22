from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^question/.+/', views.test)
]