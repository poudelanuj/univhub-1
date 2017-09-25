import datetime
import json

from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.handlers import wsgi
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from json_requests import handler
# Create your views here.
from .forms import SignupForm, AddModeratorForm, AddAdminForm, AddCounselorForm
from .models import *
from .tokens import account_activation_token


# from fcm_django.models import FCMDevice

def informationCenter():
    # id of adminGroup is 1, moderator is 2 and counselor is 3 and student is 4
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    parcel = {'adminGroup': User.objects.filter(groups__name='adminGroup'),
              'moderatorGroup': User.objects.filter(groups__name='moderatorGroup'),
              'counsellorGroup': User.objects.filter(groups__name='counsellorGroup'),
              'studentCount': User.objects.filter(groups__name='studentGroup').count(),
              'todayjoined': User.objects.filter(date_joined__range=(today_min, today_max), groups=4).count()
              }
    return parcel


def index(request):
    parcel = informationCenter()
    return render(request, 'admin-dashboard.html', parcel)


def getNotificationsPage(request):
    return render(request, "notifications.html", )


def StudentDetail(request, pk):
    student = get_object_or_404(User, pk=pk)
    documents = uploadeddocuments.objects.filter(student=student)

    return render(request, "student-detail.html", context={'student': student, 'documents': documents})


def getNotifications(request):
    user = request.user
    data = {'notifycount': Notification.objects.filter(receiver=user).count()}
    return JsonResponse(data)


def getNotificationslist(request):
    notifications = Notification.objects.filter(receiver=request.user).order_by('-created')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            current_site = get_current_site(request)
            subject = 'Activate your UnivHub Account.'
            message = render_to_string('acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # user.email_user(subject, message)
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            return render(request, 'checkemail.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        m = UserProfile(user=user)
        m1.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def getStudentslistPage(request):
    all_students = User.objects.filter(groups=4)
    paginator = Paginator(all_students, 10)
    page = request.GET.get('page', 1)  # get page or 1
    try:
        students = paginator.page(page)
        print(students)
    except PageNotAnInteger:  # if page is not an integer
        students = paginator.page(1)
        print("page not an integer")
    except EmptyPage:  # if the page number goes out of bound
        students = paginator.page(paginator.num_pages)
    print(students)
    return render(request, 'students-list.html')


def addadmin(request):
    form = AddAdminForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            errors = form.errorlist
            print(errors)
            return JsonResponse(errors)
        else:
            errors = form.errorlist
            print(errors)
            return JsonResponse(errors)

    return JsonResponse(errors)


def addmoderator(request):
    errors = {}
    form = AddModeratorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            errors = form.errorlist
            print(errors)
            return JsonResponse(errors)
        else:
            errors = form.errorlist
            print(errors)
            return JsonResponse(errors)
    return JsonResponse(errors)


def getPickupPage(request):
    print("init")
    all_pickups = pickup.objects.filter(status="pending")
    print("2nd print")
    print(all_pickups)
    all_documents = pickupdetails.objects.filter(pickupid__in=all_pickups)
    print(all_documents)
    json = {'all_pickups': all_pickups, 'all_documents': all_documents}
    return render(request, 'pickup.html', json)


def getClassesPage(request):
    print("init")
    all_classtypes = ClassType.objects.all()
    print(all_classtypes)
    all_offeredclass = OfferedClass.objects.filter(classtype__in=all_classtypes)
    print(all_offeredclass)
    json = {'all_classtypes': all_classtypes, 'all_offeredclass': all_offeredclass}
    return render(request, 'classes.html', json)


def getOffersPage(request):
    print("init")
    all_offertypes = OfferType.objects.all()
    print("2nd print")
    all_offers = Offer.objects.filter(offertype__in=all_offertypes)
    print(all_offers)
    json = {'all_offertypes': all_offertypes, 'all_offers':all_offers}
    return render(request, 'offers.html', json)


def StudentDetail(request, pk):
    student = get_object_or_404(User, pk=pk)
    documents = uploadeddocuments.objects.filter(student=student)

    print(student)
    return render(request, 'students-list.html', {'students': student})


# ajax calls handling part



def addcounselor(request):
    user = request.user
    form = AddCounselorForm(request.POST, user=user or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            errors = form.errorlist
            print(errors)
            return JsonResponse(errors)
        else:
            errors = form.errorlist
            print(errors)
            return JsonResponse(errors)

    return JsonResponse(errors)


def ajaxCallForDeleteRole(request):
    userId = request.GET.get('userId')
    User.objects.filter(id=userId).delete()
    data = informationCenter()
    reloadPortion = render_to_string('ad-adminsInformation.html', data)
    return HttpResponse(reloadPortion)


def ajaxCallForActivationRole(request):
    userId = request.GET.get('userId')
    usr = User.objects.get(id=userId)
    if (usr.is_active):
        usr.is_active = False
    else:
        usr.is_active = True
    usr.save()
    data = informationCenter()
    reloadPortion = render_to_string('ad-adminsInformation.html', data)
    return HttpResponse(reloadPortion)


def jsonHandler(request: wsgi.WSGIRequest):
    print("Json Request")
    # devices = FCMDevice.objects.all()
    #
    # print(devices.send_message(title="Title", body="Message"))
    # print(devices.send_message(title="Title", body="Message", data={"test": "test"}))
    # print(devices.send_message(data={"test": "Why not working?"}))

    if request.is_ajax():
        json_data = json.loads(request.body.decode(encoding='UTF-8'))
        response = handler.handle_request(json_data)
        print("Raw json data :", request.body)
        # safe=False means array also can be returned as response
        return response


def ajaxRemovePickupDocument(request):
    docId = request.GET.get('documentID')
    print("document-id:" + docId)
    print(pickupdetails.objects.filter(documentid=docId))
    # pickupdetails.objects.filter(documentid=docId).delete()
    all_pickups = pickup.objects.filter(status="pending")
    all_documents = pickupdetails.objects.filter(pickupid__in=all_pickups)
    json = {'all_pickups': all_pickups, 'all_documents': all_documents}
    reloadPortion = render_to_string('pickup.html', json)
    return HttpResponse(reloadPortion)
