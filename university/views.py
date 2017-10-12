from django.shortcuts import render
from .models import *
import sys
from django.http import HttpResponse, JsonResponse, Http404
import traceback


# Create your views here.
def admission_page():
    print("admission_page")
    return None


def scholarship_page():
    print("scholarship_page")
    return None


def overview_page():
    print("overview_page")
    return None


def course_page():
    print("course_page")
    return None


def detail_page(request, university_id):
    print("detail_page")
    # TODO add try except clauses
    university = University.objects.get(pk=university_id)
    address = UniversityAddress.objects.get(university=university)
    return render(request, 'index.html', context={'university': university, "address": address})


def index_page(request, ):
    print("index_page")
    return None


def course_detail_page(request, university_id, course_id):
    print("Detail_page")
    try:
        university = University.objects.get(pk=university_id)
        course = SubMajorTitle.objects.get(pk=course_id)
        submajor = UniversitySubMajor.objects.get(university=university,
                                                  title=course)
    except:
        print("Invalid university or course id in course_detail_patg", file=sys.stderr)
        response = JsonResponse({"success": False})
        response.status_code = 404
        return response
    return JsonResponse(submajor.get_detail_info())


def course_info_page(request, university_id, course_id):
    print("course_info_page")
    return None
