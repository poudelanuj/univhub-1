from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views


urlpatterns = [
    url(r'pickup.html', views.getPickupPage),
    url(r'classes.html', views.getClassesPage),
    url(r'offers.html', views.getOffersPage),
    url(r'students-list.html', views.getStudentslistPage),
    url(r'notifications.html', views.getNotificationsPage),
    url(r'^admin-dashboard', views.index, name="admin-dashboard"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^documentupload/$', views.showdocumentuploadtest, name='documentuploadtest'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^passwordchangeform/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.passwordchangeform, name='passwordchangeform'),
    url(r'^passwordchange/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.passwordchange, name='passwordchange'),
    url(r'^addadmin/$', views.addadmin, name='addadmin'),
    url(r'^addmoderator/$', views.addmoderator, name='addmoderator'),
    url(r'^addcounselor/$', views.addcounselor, name='addcounselor'),

    url(r'^jsonhandler.django(.*)', views.jsonHandler),
    url(r'^requesthandler/(?P<action>\w+)/(?P<operation>\w+)', views.jsonHandler),

    url(r'^ajax/CallForDeleteRole/$', views.ajaxCallForDeleteRole, name='ajaxCallForDeleteRole'),
    url(r'^ajax/CallForActivationRole/$', views.ajaxCallForActivationRole, name='ajaxCallForActivationRole'),
    url(r'^ajax/ajaxRemovePickupDocument/$', views.ajaxRemovePickupDocument, name='ajaxRemovePickupDocument'),
]
