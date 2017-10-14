from django.conf.urls import include
from django.conf.urls import url
from . import views

university_id = r'^(?P<university_id>\d+)/'

urlpatterns = [
    url(r'index.html', views.index_page),
    url(university_id + r'detail\.html', views.detail_page),
    url(university_id + r'courses.html', views.course_page),
    url(university_id + r'overview.html', views.overview_page),
    url(university_id + r'scholarship_detail\.html', views.scholarship_page),
    url(university_id + r'admission.html', views.admission_page),
    url(university_id + r'course/(?P<course_id>[a-z0-9_A-Z]+)/info.html', views.course_info_page),
    url(university_id + r'course/(?P<course_id>[a-z0-9_A-Z]+)/detail.html', views.course_detail_page),
    #url(university_id + r'^info.html', views.detail_page),
    #url(university_id + ".*", views.detail_page),
    url(".*",views.index_page)
]
