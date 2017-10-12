from sadmin.models import *
# from sadmin.models import UniversityBasicInfo

from django.http import JsonResponse


def info_university(request):
    universities = University.objects.all();
    univ_list = []
    for university in universities:
        dic = {
            'id': university.pk,
            'name': university.name,
            'logo_url': university.logo_url,
            'mainline': university.main_line,
            'highlights': university.get_highlights(),
            'world_ranking': university.get_world_ranking(),
            'courses': UniversitySubMajor.get_chain_for_university(university)
        }
        univ_list.append(dic)
    return JsonResponse(univ_list, safe=False)


def course_university(request):
    uid = request['university_id']
    if 'course_id' in request:
        pass



def overview_university(request):
    pass


def admission_university(request):
    pass


def scholarship_university(request):
    pass


def livingcost_university(request):
    pass
