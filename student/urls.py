from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'profile/create/submajor.html', views.ProfileSetupSubMajor.as_view()),
    url(r'^detail/(?P<pk>\d+)/', views.StudentDetail),
    url(r'uploadeddocuments/(?P<student_id>\d+)', views.getStudentUploadedDocuments),
    url(r'applieduniversities/(?P<student_id>\d+)', views.getStudentAppliedUniversities),
    url(r'classes/(?P<student_id>\d+)', views.getStudentRegisteredClasses),

]
