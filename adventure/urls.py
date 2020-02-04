from django.conf.urls import url
from django.urls import path, include
from . import views
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    path('', views.index, name='index'),
]
