from django.http import JsonResponse
from sadmin.models import *

def register_offer(request):

    return JsonResponse({'return': True, 'reason': "You are registered"})


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
                       "validity": offer.validity})
    # , "status": offerclass.status

    return JsonResponse(json, safe=False);

