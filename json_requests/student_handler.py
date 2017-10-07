from django.http import JsonResponse

from sadmin.models import *
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect



def login_student(request):
    print("Logging In..")
    logout(request)
    un = pw = ''
    if request.POST:
        un = request.POST['username']
        pw = request.POST['password']

        user = authenticate(username=un, password=pw)
        if user is not None:
            print("User found")
            if user.is_active:
                login(request, user)
                request.session.set_expiry(86400)
                return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': "Username and Password does not match."})
    else:
        return render(request, 'login.html')


def logout_student(request):
    #todo
    #logout operation
    return None


def edit_profile(request):
    # todo
    # editprofile
    return None