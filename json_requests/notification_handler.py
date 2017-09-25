import json
from django.http import JsonResponse
from sadmin.models import Notification
from django.db import models

def handle(request, operation):
    if operation in operations:
        return operations['operation'](request)
    else:
        return JsonResponse({'status':'Error','reason':"Invalid operation specified :"+operation})

def create_notification(request):
    try:
        notification = Notification(
            title = request['title'],
            message = request['details',],
            type = request['notification_type'],
            web_url = (request['web_url'] if 'web_url' in request else None),
            map_url = (request['map_url'] if 'map_url' in request else None),
            created = models.DateTimeField.auto_now,
            read = False
        )
        notification.save()
        return JsonResponse({'succes': True,})
    except Exception:
        return JsonResponse({'succes': False,})




operations={
    'crate':create_notification
}