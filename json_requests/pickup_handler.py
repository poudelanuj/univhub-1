from django.http import JsonResponse
from sadmin.models import *


def create_pickup(request):
    try:
        doctype = UploadedDocument.objects.get(docname=request['document_included'][0]).doctype
        docfor = DocumentType.objects.get(name=doctype).documentfor
        pickup = Pickup(
            location=(request['location'] if 'location' in request else None),
            map_url=(request['map_url'] if 'map_url' in request else None),
            document_for=DocumentFor.objects.get(documentforname=docfor),
            pickup_of=User.objects.get(pk=request['user_id'])
        )
        pickup.save()

        for docs in request['document_included']:
            pickupdetail = PickupDetail(
                document=UploadedDocument.objects.get(docname=docs),
                pickup=pickup
            )
            pickupdetail.save()
        return JsonResponse({'success': True, })
    except Exception as e:
        print("Caught a Exception", *e.args)
        return JsonResponse({'success': False, 'Reason': "Error processing data"})


def list_pickup(request):
    uploadeddocs = UploadedDocument.objects.filter(student=request['user_id'])

    json = []
    for docs in uploadeddocs:
        docfor = DocumentType.objects.get(name=docs.doctype).documentfor
        document_for = DocumentFor.objects.get(documentforname=docfor)
        json.append({"document_name": docs.docname,
                     "document_for": document_for.documentforname
                     })

    return JsonResponse(json, safe=False)
