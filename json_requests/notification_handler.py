import json
from django.http import JsonResponse

def handle(request):
    return JsonResponse({'succes': True, 'uid':1})
