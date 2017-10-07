from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'login.django', views.login),
    url(r'.*', views.LoginView.as_view()),

]
