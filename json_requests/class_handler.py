from django.http import JsonResponse
from sadmin.models import *

def register_class(request):
    return JsonResponse({'return': True, 'reason': "You are registered"})


def list_class(request):
    offeredclass = OfferedClass.objects.all()

    json = []
    for offerclass in offeredclass:
        json.append({"name": offerclass.name,
                      "classtype": offerclass.classtype.title,
                       "startdate": offerclass.startdate,
                       "enddate": offerclass.enddate,
                      "discountpercent" : offerclass.discountpercent,
                      "scholarshippercent" : offerclass.scholarshippercent,
                        "tutor": offerclass.tutor.name,
                       "starttime": offerclass.starttime,
                       "endtime": offerclass.endtime,
                        "location": offerclass.location,
                     "status": "Register"})

    return JsonResponse(json, safe=False);

