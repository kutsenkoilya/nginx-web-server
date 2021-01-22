
from django.urls import path
from views import test

urlpatterns = [
    path(r'^(\d)+$', test, name='test'),
]
