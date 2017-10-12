from sadmin.models import *
# from sadmin.models import UniversityBasicInfo

from django.http import JsonResponse


def info_university(request):
    universities = University.objects.all();
    univ_list = []
    for university in universities:
        address = UniversityAddress.objects.filter(university=university, is_main=True)[0]
        sub_majors, count = UniversitySubMajor.get_chain_for_university(university)
        dic = {
            'id': university.pk,
            'name': university.name,
            'logo_url': university.logo_url,
            'mainline': university.main_line,
            'highlights': university.highlights(),
            'location': {
                'country': address.country,
                'state': address.state,
                'city': address.city,
                'street': address.street,
                'postal_code': address.postal_code
            },
            "scholarship": "false",
            "my_course": ["Course1", "Course2"],
            'world_ranking': university.get_world_ranking(),
            'courses': sub_majors,
            'course_count': count
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
