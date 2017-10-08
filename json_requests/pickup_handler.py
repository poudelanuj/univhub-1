from django.http import JsonResponse
from sadmin.models import *


def create_pickup(request):
    pickup = Pickup(
        location=(request['location'] if 'location' in request else None),
        map_url=(request['map_url'] if 'map_url' in request else None),
        document_for=DocumentFor.objects.filter(documentforname=request['document_for']),
        pickup_of=request['user_id']
    )
    pickup.save()

    pickupdetail = PickupDetail(
        documentid=UploadedDocument.objects.get(docname=request['document_included']),
        pickupid=pickup.id
    )
    pickupdetail.save()

    return JsonResponse({'succes': True, })


def list_pickup(request):
    json = [{"document_name": "SLC Transcript", "document_for": "Offer Letter"},
            {"document_name": "Recommendation Letter", "document_for": "Offer Letter"},
            {"document_name": "Bank Statement", "document_for": "Financial Verification"},
            {"document_name": "Property Valuation", "document_for": "Financial Verification"},
            {"document_name": "Passport", "document_for": "Getting Visa"},
            {"document_name": "Citizenship", "document_for": "Getting Visa"}
            ]

    return JsonResponse(json, safe=False);

