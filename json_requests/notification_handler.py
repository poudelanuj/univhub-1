import json
from django.http import JsonResponse
from sadmin.models import Notification
from django.db import models
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
import traceback
from sadmin.models import Notification, NotificationType


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
        return JsonResponse({'succes': False, 'Reason': "Error processing data"})


def filter_notification(request):
    try:
        print(request)
        filters = request['filter_by']
        duration=request['duration']
        if 'type' in filters:
            if 'duration' in filters:
                pass
            filtered = Notification.objects.filter(Type=request['type'])
            return render(request['request'], 'notification_list.html', context={'type': NotificationType.objects.all(), 'notifications': filtered})
        else:
            raise Exception("Duration not specified")
    except Exception as e:
        print("Exception", *e.args)
        traceback.print_exc()
        return JsonResponse({'succes': False, 'Reason': "Error processing data on notification filter"})


def detail_notification(request):
    try:

        Notification.objects.filter(Type=type)
    except Exception as e:
        print("Exception", *e.args)
        traceback.print_exc(e);
        return JsonResponse({'succes': False, 'Reason': "Error processing data on notification filter"})
