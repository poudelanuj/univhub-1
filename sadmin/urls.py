from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^',views.index),
    url(r'^pickup/',views.getPickup),
]
