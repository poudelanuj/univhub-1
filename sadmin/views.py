from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User, Group
from . import models
from django.template import Context
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.



def informationCenter():
	#id of adminGroup is 1, moderator is 2 and counselor is 3 and student is 4
	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
	parcel={'adminGroup':User.objects.filter(groups__name='adminGroup'), 
	'moderatorGroup':User.objects.filter(groups__name='moderatorGroup'),
	'counsellorGroup':User.objects.filter(groups__name='counsellorGroup'),
	'studentCount': User.objects.filter(groups__name='studentGroup').count(),
	'todayjoined': User.objects.filter(date_joined__range = (today_min, today_max) , groups=4).count()
	}
	return parcel



def index(request):
	parcel= informationCenter()
	return render(request, 'admin-dashboard.html',parcel)


def getNotificationsPage(request):
	return render(request,"notifications.html",)



def getStudentslistPage(request):
    all_students = User.objects.filter(groups=4)
    paginator= Paginator(all_students,10)
    page = request.GET.get('page',1) #get page or 1
    try:
       students = paginator.page(page)
       print (students)
    except PageNotAnInteger:				 #if page is not an integer
       students = paginator.page(1)
       print ("page not an integer")
    except EmptyPage:						 #if the page number goes out of bound
       students = paginator.page(paginator.num_pages)

    print (students)
    return render(request, 'students-list.html',{'students':students})



def getPickupPage(request):
	all_pickups = models.pickup.objects.filter(status="pending")
	print (all_pickups)
	all_documents = models.pickupdetails.objects.filter(pickupid__in=all_pickups )
	print (all_documents)

	json = {'all_pickups':all_pickups, 'all_documents':all_documents}
	return render (request, 'pickup.html', json)

	
def StudentDetail(request,pk):
    student=get_object_or_404(User,pk=pk)
    documents=Document.objects.filter(student=student)

    print (students)
    return render(request, 'students-list.html',{'students':students})



def getPickupPage(request):
	all_pickups = models.pickup.objects.filter(status="pending")
	print (all_pickups)
	all_documents = models.pickupdetails.objects.filter(pickupid__in=all_pickups )
	print (all_documents)

	json = {'all_pickups':all_pickups, 'all_documents':all_documents}
	return render (request, 'pickup.html', json)




#ajax calls handling part



def ajaxCallForDeleteRole(request):
	userId = request.GET.get('userId')
	User.objects.filter(id=userId).delete()
	data=informationCenter()
	reloadPortion= render_to_string('ad-adminsInformation.html', data)
	return HttpResponse(reloadPortion)
	


def ajaxCallForActivationRole(request):
	userId = request.GET.get('userId')
	usr = User.objects.get(id=userId)
	if(usr.is_active):
		usr.is_active=False
	else:
		usr.is_active=True
	usr.save()
	data=informationCenter()
	reloadPortion=render_to_string('ad-adminsInformation.html', data)
	return HttpResponse(reloadPortion)


def ajaxRemovePickupDocument(request):
	docId = request.GET.get('documentID')
	print ("document-id:" + docId)
	print (models.pickupdetails.objects.filter(documentid=docId))
	#models.pickupdetails.objects.filter(documentid=docId).delete()
	all_pickups = models.pickup.objects.filter(status="pending")
	all_documents = models.pickupdetails.objects.filter(pickupid__in=all_pickups )
	json = {'all_pickups':all_pickups, 'all_documents':all_documents}
	reloadPortion = render_to_string('pickup.html',json)
	return HttpResponse(reloadPortion)
