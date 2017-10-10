from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic.edit import FormView

from sadmin.models import *


# Create your views here.


class ProfileSetupSubMajor(FormView):
    template_name = 'profile_sub_major_select.html'

    class Void(object):
        pass

    def get(self, request, *args, **kwargs):
        sub_major = SubMajor.objects.all()
        # get all the list of major and submajor
        majors = {}
        for sub in sub_major:
            uni_count = ReqMap.objects.filter(submajor=sub.id).count()
            major = str(sub.major)
            if major in majors:
                majors[major].sub_majors.append(self.Void())
            else:
                majors[major] = self.Void()
                majors[major].name = major
                majors[major].sub_majors = [self.Void()]
            majors[major].sub_majors[-1].name = sub.sub_major_name
            majors[major].sub_majors[-1].uni_count = uni_count
            majors[major].sub_majors[-1].id = sub.id
        for major in majors.values():
            major.sub_major_count = len(major.sub_majors)

        # get all the list of major and submajor

        return render(request, self.template_name, context={'majors': majors.values()})


def StudentDetail(request, pk):
    student = get_object_or_404(User, pk=pk)
    documents = UploadedDocument.objects.filter(student=student)
    return render(request, 'student-profile.html', {'student': student})


def getStudentUploadedDocuments(request, student_id):
    student = get_object_or_404(User, pk=student_id)
    documents = UploadedDocument.objects.filter(student=student)
    return render(request, 'studentuploadeddocuments.html', {'documents': documents})


def getStudentAppliedUniversities(request, student_id):
    student = get_object_or_404(User, pk=student_id)


def getStudentRegisteredClasses(request, student_id):
    student = get_object_or_404(User, pk=student_id)
    classes = RegisteredClass.objects.filter(user=student)
    return render(request, 'studentuploadeddocuments.html', {'classes': classes})


def getStudentNotice(request, student_id):
    student = get_object_or_404(User, pk=student_id)
    notifications = Notification.objects.filter(receiver=student)
    return render(request, 'studentuploadeddocuments.html', {'notifications': notifications})


def editStudentProfile(request,student_id):
    student = get_object_or_404(User, pk=student_id)
    return render(request,'edit-profile.html',context={'student':student})