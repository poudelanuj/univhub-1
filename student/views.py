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


# Create your views here.
def login(request):
    pass;

class ProfileSetupSubheader(FormView):
    template_name = 'profile_sub_major_select.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name)
