
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'pickup.html',views.getPickupPage),

    url(r'students-list.html',views.getStudentslistPage),
    url(r'notifications.html',views.getNotificationsPage),
    url(r'^admin-dashboard', views.index,name="admin-dashboard"),
    url(r'^studentdetail/(?P<pk>\d+)/',views.StudentDetail),
    url(r'^getnotifications/',views.getNotifications,name="getnotifications"),
    url(r'^getnotificationslist/',views.getNotificationslist,name="getnotificationslist"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	url(r'^addadmin/$', views.addadmin, name='addadmin'),
    url(r'^addmoderator/$', views.addmoderator, name='addmoderator'),
    # url(r'^addcounselor/$', views.addcounselor, name='addcounselor'),

    url(r'^jsonhandler.django',views.jsonHandler),

    url(r'^ajax/CallForDeleteRole/$', views.ajaxCallForDeleteRole, name='ajaxCallForDeleteRole'),
    url(r'^ajax/CallForActivationRole/$', views.ajaxCallForActivationRole, name='ajaxCallForActivationRole'),

    url(r'^ajax/ajaxRemovePickupDocument/$', views.ajaxRemovePickupDocument, name='ajaxRemovePickupDocument'),
]
