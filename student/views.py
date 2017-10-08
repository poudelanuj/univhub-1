from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from sadmin.models import AdminProfile
import json

from sadmin.models import SubMajor, Major, ReqMap


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
