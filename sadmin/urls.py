
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'pickup.html',views.getPickupPage),
    url(r'students-list.html',views.getStudentslistPage),
    url(r'notifications.html',views.getNotificationsPage),
    url(r'^admin-dashboard', views.index),
    url(r'^noticecreate/', views.noticecreate),

    url(r'^studentdetail/(?P<pk>\d+)/',views.StudentDetail),
    url(r'^getnotifications/',views.getNotifications),
    url(r'^jsonhandler.django',views.jsonHandler),
]
