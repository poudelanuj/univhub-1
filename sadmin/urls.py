
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [

	#dashboard side tabs
    url(r'pickup.html',views.getPickupPage),
    url(r'students-list.html',views.getStudentslistPage),
    url(r'notifications.html',views.getNotificationsPage),
    url(r'^admin-dashboard', views.index, name="admin-dashboard"),


    #dashboard buttons
    url(r'^ajax/CallForDeleteRole/$', views.ajaxCallForDeleteRole, name='ajaxCallForDeleteRole'),
    url(r'^ajax/CallForActivationRole/$', views.ajaxCallForActivationRole, name='ajaxCallForActivationRole'),

    url(r'^ajax/ajaxRemovePickupDocument/$', views.ajaxRemovePickupDocument, name='ajaxRemovePickupDocument'),
]
