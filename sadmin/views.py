from django.shortcuts import render
from notifications.signals import notify
# Create your views here.
from django.shortcuts import get_object_or_404
from .models import Document
from django.contrib.auth.models import User
def index(request):
    return render(request, "admin-dashboard.html")
def noticecreate(request):

    notify.send(request.user,recipient=request.user, verb='was saved')

def getNotificationsPage(request):
    return render(request,"notifications.html",)
def getPickupPage(request):
    return render(request,"pickup.html")
def getStudentslistPage(request):
    return render(request,"students-list.html")
def StudentDetail(request,pk):
    student=get_object_or_404(User,pk=pk)
    documents=Document.objects.filter(student=student)

    return render(request,"student-detail.html",context={'student':student,'documents':documents})
def getNotifications(request):
    user=request.user
    user.notifications.unread
