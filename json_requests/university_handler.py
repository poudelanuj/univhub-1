from sadmin.models import *
# from sadmin.models import UniversityBasicInfo

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def info_university(request):
    if 'university_id' in request:
        uid = request['university_id']
        University.objects.filter(id=uid)
        return JsonResponse(University.objects.get(id=uid).brief_info())
    elif 'bound' in request:
        bound = request['bound']
    else:
        bound = (0, 5)
    universities = University.objects.all()[bound[0]:bound[1]]
    univ_list = []
    for university in universities:
        univ_list.append(university.brief_info())
    return JsonResponse(univ_list, safe=False)

def course_university(request):
    uid = request['university_id']
    if 'course_id' in request:
        cid = request['course_id']
        return JsonResponse(UniversitySubMajor.objects.get(university=uid, title=cid).get_brief_info())
    elif 'bound' in request:
        bound = request['bound']
    else:
        bound = [0, 5]
    submajors=UniversitySubMajor.objects.filter(university=uid)[bound[0]:bound[1]]
    return JsonResponse([x.get_brief_info() for x in submajors],safe=False)

def overview_university(request):
    pass


def admission_university(request):
    pass


def scholarship_university(request):
    pass


def livingcost_university(request):
    pass


def course_info(request):
    pass
