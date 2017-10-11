import traceback

from django.http import JsonResponse
from django.shortcuts import render

from sadmin.models import Notification, NotificationType


def dashboard_page_notification(request):
    return render


def create_notification(request):
    notification = Notification(
        title=request['title'],
        message=request['details'],
        type=NotificationType.objects.filter(pk=request['notification_type'])[0],
        web_url=(request['web_url'] if 'web_url' in request else None),
        map_url=(request['map_url'] if 'map_url' in request else None),
        read=False
    )
    notification.save()
    return JsonResponse({'succes': True, })


def filter_notification(request):
    print(request)
    filters = request['filter_by']
    duration = request['duration']
    if 'type' in filters:
        if 'duration' in filters:
            pass
        filtered = Notification.objects.filter(type=request['type'])
        return render(request['request'], 'notification_list.html',
                      context={'type': NotificationType.objects.all(), 'notifications': filtered})
    else:
        raise Exception("Duration not specified")


def detail_notification(request):
    try:
        Notification.objects.filter(Type=type)
    except Exception as e:
        print("Exception", *e.args)
        traceback.print_exc(e)
        return JsonResponse({'succes': False, 'Reason': "Error processing data on notification filter"})


def bell_drop_list_notification(request):
    notifications = Notification.objects.filter(receiver=request.user.pk).order_by('-created')
    return render(request, 'notification_drop.html', {'notifications': notifications})


def live_count_notification(request):
    print(request.user)
    user = request.user
    data = {'notifycount': Notification.objects.filter(receiver=user).count()}
    return JsonResponse(data)
