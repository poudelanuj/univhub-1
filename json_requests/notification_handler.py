import json
from django.http import JsonResponse
from sadmin.models import Notification
from django.db import models


def create_notification(request):
    try:
        notification = Notification(
            title=request['title'],
            message=request['details'],
            Type=request['notification_type'],
            web_url=(request['web_url'] if 'web_url' in request else None),
            map_url=(request['map_url'] if 'map_url' in request else None),
            read=False
        )
        notification.save()
        return JsonResponse({'succes': True, })
    except Exception as e:
        print("Exception", *e.args)
        return JsonResponse({'succes': False, 'Reason':"Error processing data"})
