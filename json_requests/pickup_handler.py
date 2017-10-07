from django.http import JsonResponse

from sadmin.models import *
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect


def scheduledate(request):
    print("POST data: ")
    print(request.POST)
    return None
