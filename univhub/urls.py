
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import notifications.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'sadmin/',include('sadmin.urls')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
