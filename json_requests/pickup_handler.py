from django.http import JsonResponse
from sadmin.models import *


def list_pickup(request):
    json = [{"document_name": "SLC Transcript", "document_for": "Offer Letter"},
            {"document_name": "Recommendation Letter", "document_for": "Offer Letter"},
            {"document_name": "Bank Statement", "document_for": "Financial Verification"},
            {"document_name": "Property Valuation", "document_for": "Financial Verification"},
            {"document_name": "Passport", "document_for": "Getting Visa"},
            {"document_name": "Citizenship", "document_for": "Getting Visa"}
            ]

    return JsonResponse(json, safe=False);

