from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect,JsonResponse
from sadmin.models import *
from .forms import *
from django.urls import reverse

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
    usr = get_object_or_404(User, pk=pk)
    spnsr = Sponsor.objects.filter(sponsorof=pk)
    # documents = UploadedDocument.objects.filter(student=student)
    return render(request, 'student-profile.html', {'user': usr, 'sponsor': spnsr})


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


def editStudentProfile(request, student_id):
    student = get_object_or_404(User, pk=student_id)
    if request.method == 'POST':
        print('1')
        print(request.POST.get('firstname'))
        print('2')
        form=StudentEditForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            student.first_name=form.cleaned_data.get('firstname')
            student.student.middle_name=form.cleaned_data.get('middlename')
            student.last_name=form.cleaned_data.get('lastname')
            student.email=form.cleaned_data.get('email')
            student.student.gender = form.cleaned_data.get('gender')
            student.student.dob_np=form.cleaned_data.get('dobnp')
            student.student.dob_en=form.cleaned_data.get('doben')
            student.student.phone1=form.cleaned_data.get('phone1')
            student.student.phone2=form.cleaned_data.get('phone2')
            student.student.phone3=form.cleaned_data.get('phone3')
            addr1=Address.objects.create(district=get_object_or_404(District,districtname=form.cleaned_data.get('district')),city=form.cleaned_data.get('city'),
                                         AddressLine1=form.cleaned_data.get('addressline1'),
                                         AddressLine2=form.cleaned_data.get('addressline2'),
                                         AddressLine3=form.cleaned_data.get('addressline3'),
                           )
            student.student.temp_address=addr1
            addr2=Address.objects.create(district=get_object_or_404(District,districtname=form.cleaned_data.get('permdistrict')),city=form.cleaned_data.get('permcity'),
                                         AddressLine1=form.cleaned_data.get('permaddressline1'),
                                         AddressLine2=form.cleaned_data.get('permaddressline2'),
                                         AddressLine3=form.cleaned_data.get('permaddressline3'),
                           )
            student.student.perm_address=addr2
            student.student.save()
            student.save()
            return  HttpResponseRedirect(reverse('studentdetail',args=(student.id,)))
        else:
            print(form.errors)
            return JsonResponse({'success':False})
    else:
        return render(request, 'edit-profile.html', {'user': student,})

