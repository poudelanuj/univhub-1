from django.http import JsonResponse
from sadmin.models import *


def register_class(request):
    try:
        registeredclass = RegisteredClass(
            user=User.objects.only('id').get(id=request['user_id']),
            offeredclass=OfferedClass.objects.only('id').get(id=request['user_id'])
        )
        print(registeredclass.user)
        print(registeredclass.offeredclass)
        registeredclass.save()
        return JsonResponse({'success': True})
    except Exception as e:
        print("Caught a Exception", *e.args)
        return JsonResponse({'success': False, 'Reason': "Error processing data"})


def list_offer(request):
    offers = Offer.objects.all()

    # json = {"title":"title"}
    json = []
    for offer in offers:
        json.append({"title": offer.title,
                      "description": offer.description,
                       "offertype": offer.offertype.title,
                       "offerinclass": None if offer.offerinclass is None else offer.offerinclass.name,
                     "classprice": None if offer.offerinclass is None else offer.offerinclass.price,
                      "discountpercent": offer.discountpercent,
                      "scholarshippercent": offer.scholarshippercent,
                        "university": None if offer.university is None else offer.university.name,
                       "validity": offer.validity,
                     "status": "Register"})
    # , "status": offerclass.status

    return JsonResponse(json, safe=False);

