
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [

    url(r'notifications.html',views.notifications),
    url(r'^admin-dashboard', views.index),
]
