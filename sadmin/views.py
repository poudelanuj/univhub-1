import json
from datetime import datetime

from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.handlers import wsgi
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from json_requests import handler
# Create your views here.
from .forms import SignupForm, AddModeratorForm, AddAdminForm, AddCounselorForm
from .models import *
from .tokens import account_activation_token
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import datetime
import traceback


# from fcm_django.models import FCMDevice

def informationCenter():
    # id of adminGroup is 1, moderator is 2 and counselor is 3 and student is 4
    parcel = {'adminGroup': User.objects.filter(groups__name='adminGroup'),
              'moderatorGroup': User.objects.filter(groups__name='moderatorGroup'),
              'counsellorGroup': User.objects.filter(groups__name='counsellorGroup'),
              'studentCount': User.objects.filter(groups__name='studentGroup').count(),
              'todayjoined': User.objects.filter(date_joined__day=datetime.now().day, groups=4).count()
              }
    return parcel


def index(request):
    parcel = informationCenter()
    return render(request, 'admin-dashboard.html', parcel)


def getNotificationsPage(request):
    print("size of notification", len(Notification.objects.all()))
    return render(request, "notifications.html",
                  context={'types': NotificationType.objects.all(), 'notifications': Notification.objects.all()})


def StudentDetail(request, pk):
    student = get_object_or_404(User, pk=pk)
    documents = UploadedDocument.objects.filter(student=student)

    return render(request, "student-detail.html", context={'student': student, 'documents': documents})


def getNotifications(request):
    user = request.user
    data = {'notifycount': Notification.objects.filter(receiver=user).count()}
    return JsonResponse(data)


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
            print("form valid")
            newuser = form.save()
            print("form valid 2")

            errors = form.errorlist
            errors.update(dict(form.errors.items()))
            current_site = get_current_site(request)
            subject = 'Activate your UnivHub Account.'
            message = render_to_string('password_change_email.html', {
                'user': newuser, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
                'token': account_activation_token.make_token(newuser),
            })
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            Notification.objects.create(receiver=get_object_or_404(User, pk=1), sender=newuser,
                                        title="New Admin Creation",
                                        message="New admin has been created", created=datetime.datetime.now())
            return JsonResponse(errors)
        else:
            errors = form.errorlist
            errors.update(dict(form.errors.items()))
            return JsonResponse(errors)

    return JsonResponse(errors)


def addmoderator(request):
    form = AddModeratorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            newuser = form.save()
            errors = form.errorlist
            errors.update(dict(form.errors.items()))
            current_site = get_current_site(request)
            subject = 'Activate your UnivHub Account.'
            message = render_to_string('password_change_email.html', {
                'user': newuser, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
                'token': account_activation_token.make_token(newuser),
            })
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            Notification.objects.create(receiver=get_object_or_404(User, pk=1), sender=newuser,
                                        title="New Moderator Creation",
                                        message="New moderator has been created", created=datetime.datetime.now())
            return JsonResponse(errors)
        else:
            errors = form.errorlist
            errors.update(dict(form.errors.items()))
            return JsonResponse(errors)
    return JsonResponse(errors)


def getPickupPage(request):
    print("init")
    all_Pickups = Pickup.objects.filter(status="pending")
    print("2nd print")
    print(all_Pickups)
    all_documents = PickupDetail.objects.filter(Pickupid__in=all_Pickups)
    print(all_documents)
    json = {'all_Pickups': all_Pickups, 'all_documents': all_documents}
    return render(request, 'Pickup.html', json)


def getClassesPage(request):
    sunday = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday() + 1)
    all_classtypes = ClassType.objects.all()
    offeredclass_today = OfferedClass.objects.filter(created__day=datetime.datetime.now().day)
    offeredclass_week = OfferedClass.objects.filter(created__gte=sunday)
    offeredclass_month = OfferedClass.objects.filter(created__month=datetime.datetime.now().month)
    json = {'all_classtypes': all_classtypes,
            'offeredclass_today': offeredclass_today,
            'offeredclass_week': offeredclass_week,
            'offeredclass_month': offeredclass_month}
    return render(request, 'classes.html', json)


def getOffersPage(request):
    sunday = datetime.now() - datetime.timedelta(days=datetime.now().weekday() + 1)
    all_offertypes = OfferType.objects.all()
    print(datetime.now().day)
    print(datetime.now().month)
    print(datetime.now())
    print(sunday)
    offer_today = Offer.objects.filter(created__day=datetime.now().day)
    offer_week = Offer.objects.filter(created__gte=sunday)
    offer_month = Offer.objects.filter(created__month=datetime.now().month)
    json = {'all_offertypes': all_offertypes,
            'offer_today': offer_today,
            'offer_week': offer_week,
            'offer_month': offer_month}
    return render(request, 'offers.html', json)


def StudentDetail(request, pk):
    student = get_object_or_404(User, pk=pk)
    documents = UploadedDocument.objects.filter(student=student)

    print(student)
    return render(request, 'students-list.html', {'students': student})


# ajax calls handling part

def addcounselor(request):
    user = request.user
    form = AddCounselorForm(request.POST, user=user or None)
    if request.method == 'POST':
        if form.is_valid():
            newuser = form.save()
            errors = form.errorlist
            errors.update(dict(form.errors.items()))
            current_site = get_current_site(request)
            subject = 'Activate your UnivHub Account.'
            message = render_to_string('password_change_email.html', {
                'user': newuser, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
                'token': account_activation_token.make_token(newuser),
            })
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            Notification.objects.create(receiver=get_object_or_404(User, pk=1), sender=newuser,
                                        title="New Counselor Creation",
                                        message="New Counselor has been created", created=datetime.datetime.now())
            return JsonResponse(errors)
        else:
            errors = form.errorlist
            errors.update(dict(form.errors.items()))
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


@csrf_exempt
def jsonHandler(request: wsgi.WSGIRequest, action=None, operation=None):
    type = request.META.get('CONTENT_TYPE')
    try:
        # print the details
        if type == 'application/json':
            try:
                # try to convert body into json object
                json_data = json.loads(request.body.decode(encoding='UTF-8'))

                # if the request is from direct url
                if action is not None and operation is not None:
                    json_data['action'] = {'data': action, 'operation': operation}
                json_data['request'] = request
                return handler.handle_request(json_data)

            except Exception as e:
                # maybe the data is not json.
                # try other methodse
                print(request.POST)
                print(request.GET)
                response = JsonResponse(
                    {'status': "Error", "Reason": "Json Encryption on data failed. Invalid data sent"})
                response.status_code = 300
                return response

        elif action is not None and operation is not None:
            return handler.handle_request_direct(action, operation, request)
        else:
            response = JsonResponse({'status': "Error", "Reason": "Invalid content type on jsonHandler"})
            response.status_code = 404
            return response
    except Exception as e:
        print("Unaspected")
        response = JsonResponse({'status': "Error", "Reason": "Internal Server Error on json/request Handler"})
        response.status_code = 500
        return response


def ajaxRemovePickupDocument(request):
    docId = request.GET.get('documentID')
    print("document-id:" + docId)
    print(PickupDetail.objects.filter(documentid=docId))
    # PickupDetail.objects.filter(documentid=docId).delete()
    all_Pickups = Pickup.objects.filter(status="pending")

    all_documents = PickupDetail.objects.filter(Pickupid__in=all_Pickups)
    json = {'all_Pickups': all_Pickups, 'all_documents': all_documents}
    reloadPortion = render_to_string('Pickup.html', json)
    return HttpResponse(reloadPortion)


def passwordchangeform(request, uidb64, token):
    try:
        uid1 = uidb64
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:

        return render(request, 'passwordchangeform.html', context={'uid': uid1, 'token': token})
    else:
        return HttpResponse('Activation link is invalid!')


def passwordchange(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        password = request.POST.get("password", "")
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if account_activation_token.check_token(user, token) and user is not None:
        user.password = password
        user.save()
        login(request, user)
        return HttpResponse('Password is changed')
    else:
        return HttpResponse('Activation link is invalid!')
