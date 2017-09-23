from django.shortcuts import render
from django.core.handlers import wsgi
# from fcm_django.models import FCMDevice
from fcm.utils import get_device_model
import json
# Create your views here.
from django.shortcuts import get_object_or_404
from .models import Document
from django.contrib.auth.models import User
from django.http import JsonResponse


def index(request: wsgi.WSGIRequest):
    return render(request, "admin-dashboard.html")


def noticecreate(request):
    notify.send(request.user, recipient=request.user, verb='was saved')


def getNotificationsPage(request):
    return render(request, "notifications.html", )


def getPickupPage(request):
    return render(request, "pickup.html")


def getStudentslistPage(request):
    return render(request, "students-list.html")


def StudentDetail(request, pk):
    student = get_object_or_404(User, pk=pk)
    documents = Document.objects.filter(student=student)

    return render(request, "student-detail.html", context={'student': student, 'documents': documents})


def getNotifications(request):
    user = request.user
    user.notifications.unread


def jsonHandler(request:wsgi.WSGIRequest):
    print("Json Request")
    # devices = FCMDevice.objects.all()
    #
    # print(devices.send_message(title="Title", body="Message"))
    # print(devices.send_message(title="Title", body="Message", data={"test": "test"}))
    # print(devices.send_message(data={"test": "Why not working?"}))

    if request.is_ajax():
        if request.method == 'POST':
            json_data=json.loads(request.body.decode(encoding='UTF-8'))
            print('Raw Data: "%s"' % json_data)
            json.dumps(json_data,indent=2)

        else:
            print("Raw Data on else :", request.body)

    return JsonResponse(['yes', "it's", 'a', 'success'], safe=False)
