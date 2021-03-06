from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from sadmin.models import UploadedDocument, DocumentType


def upload_document(request):
    try:
        doctype = get_object_or_404(DocumentType, name=request.POST.get('doctype'))
        new = UploadedDocument.objects.create(student=request.user, doctype=doctype,
                                               docname=request.POST.get('docname'), file=request.FILES['file'])
        return JsonResponse({'succes': True, 'url': new.file.url})
    except Exception as e:
        print("Exception", *e.args)
        return JsonResponse({'succes': False, 'Reason': "Error processing data"})


def delete_document(request):
    try:
        doctype = get_object_or_404(DocumentType, pk=request.POST.get('docid'))
        doctype.delete()
        return JsonResponse({'succes': True, })
    except Exception as e:
        print("Exception", *e.args)
        return JsonResponse({'succes': False, 'Reason': "Error deleting document"})
