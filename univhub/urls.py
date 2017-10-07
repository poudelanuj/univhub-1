from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'sadmin/', include('sadmin.urls')),
    url(r'student/', include('student.urls')),
    url(r'auth', include('global_auth.urls')),
    url(r'', include("global_auth.urls"))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
