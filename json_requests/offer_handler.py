from django.http import JsonResponse
from sadmin.models import *


def register_offer(request):
    try:
        registeredoffer = RegisteredOffer(
            user=User.objects.get(id=request['user_id']),
            offer=Offer.objects.get(id=request['offer_id'])
        )
        print(registeredoffer.user)
        print(registeredoffer.offer)
        registeredoffer.save()
        return JsonResponse({'success': True})
    except Exception as e:
        print("Caught a Exception", *e.args)
        return JsonResponse({'success': False, 'Reason': "Error processing data"})


def status(offer):
    registeredoffer = RegisteredOffer.objects.all()
    offertype = offer.offertype.id

    if offertype is 1:
        if registeredoffer.filter(offer=offer).exists():
            return "Registered"
        else:
            return "Register"

    elif offertype is 2:
        if registeredoffer.filter(offer=offer).exists():
            return "Applied"
        else:
            return "Apply"

    else:
        pass


def list_offer(request):
    offers = Offer.objects.all()

    json = []
    for offer in offers:
        json.append({"offer_id": offer.id,
                    "title": offer.title,
                      "description": offer.description,
                       "offertype": offer.offertype.title,
                       "offerinclass": None if offer.offerinclass is None else offer.offerinclass.name,
                     "classprice": None if offer.offerinclass is None else offer.offerinclass.price,
                      "discountpercent": offer.discountpercent,
                      "scholarshippercent": offer.scholarshippercent,
                        "university": None if offer.university is None else offer.university.name,
                       "validity": offer.validity,
                     "status": status(offer)
                     })

    return JsonResponse(json, safe=False);

