from django.http import JsonResponse
from sadmin.models import *


def register_class(request):
    try:
        registeredclass = RegisteredClass(
            user=User.objects.get(id=request['user_id']),
            offeredclass=OfferedClass.objects.get(id=request['class_id'])
            # user = User.objects.only('id').get(id=request['user_id']),
        )
        print(registeredclass.user)
        print(registeredclass.offeredclass)
        registeredclass.save()
        return JsonResponse({'success': True})
    except Exception as e:
        print("Caught a Exception", *e.args)
        return JsonResponse({'success': False, 'Reason': "Error processing data"})


def status(offerclass, registeredclass):
    if registeredclass.filter(offeredclass=offerclass).exists():
        return "Registered"
    else:
        return "Register"


def list_class(request):
    offeredclass = OfferedClass.objects.all()
    registeredclass = RegisteredClass.objects.filter(user=request['user_id'])

    json = []
    for offerclass in offeredclass:
        json.append({"class_id": offerclass.id,
                    "name": offerclass.name,
                      "classtype": offerclass.classtype.title,
                       "startdate": offerclass.startdate,
                       "enddate": offerclass.enddate,
                      "discountpercent": offerclass.discountpercent,
                        "tutor": offerclass.tutor.name,
                       "starttime": offerclass.starttime,
                       "endtime": offerclass.endtime,
                        "location": offerclass.location,
                     "status": status(offerclass, registeredclass)
                     })
 
    return JsonResponse(json, safe=False);

