from sadmin.models import UniAddress
from sadmin.models import University
from sadmin.models import UniversityContent
from sadmin.models import UniversityRequirement

from django.db import models
from sadmin.models import *;
# from sadmin.models import UniversityBasicInfo

from django.http import JsonResponse

def basic_info_university(request):
    print(request.user.pk,request.user)

    universities = University.objects.all();
    univ_list = []
    for university in universities:
        dic = {
            'id': university.pk,
            'name': university.name,
            'country': university.country,
            'logo_url': university.logo_url
        }
        contents = UniversityContent.objects.filter(u=university.pk)
        univ_content = dic['contents'] = {}

        # load all the content in the
        for content in contents:
            if content.h.title not in univ_content:
                univ_content[content.h.title] = {content.sh.title: content.description}
            else:
                univ_content[content.h.title][content.sh.title] = content.description
            univ_content[content.sh.title] = content.description;

        univ_lev = dic['levels'] = {}
        subs = ReqMap.objects.filter(u=university.pk)
        for sub in subs:
            if sub.level.level_name in univ_lev:
                if sub.submajor.major.major_name in univ_lev[sub.level.level_name]:
                    univ_lev[sub.level.level_name][sub.submajor.major.major_name].append(sub.submajor.sub_major_name)
                else:
                    univ_lev[sub.level.level_name][sub.submajor.major.major_name] = [sub.submajor.sub_major_name]
            else:
                univ_lev[sub.level.level_name] = {sub.submajor.major.major_name: [sub.submajor.sub_major_name]}
        univ_list.append(dic)
    return JsonResponse(univ_list,safe=False)
