from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'sadmin/', include('sadmin.urls')),
    url(r'.*', include('global_auth.urls'))

]
