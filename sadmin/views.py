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
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from json_requests import handler
# Create your views here.
from .forms import SignupForm, AddModeratorForm, AddAdminForm, AddCounselorForm
from .models import *
from .tokens import account_activation_token
from django.views.decorators.csrf import csrf_exempt


# from fcm_django.models import FCMDevice

def informationCenter():
    # id of adminGroup is 1, moderator is 2 and counselor is 3 and student is 4
    parcel = {'adminGroup': User.objects.filter(groups__name='adminGroup'),
              'moderatorGroup': User.objects.filter(groups__name='moderatorGroup'),
              'counsellorGroup': User.objects.filter(groups__name='counsellorGroup'),
              'studentCount': User.objects.filter(groups__name='studentGroup').count(),
              'todayjoined': User.objects.filter(date_joined__day=datetime.date.today().day, groups=4).count()
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
    sunday = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday() + 1)
    all_classtypes = ClassType.objects.all()
    offeredclass_today = OfferedClass.objects.filter(created__day=datetime.date.today().day)
    offeredclass_week = OfferedClass.objects.filter(created__gte=sunday)
    offeredclass_month = OfferedClass.objects.filter(created__month=datetime.date.today().month)
    json = {'all_classtypes': all_classtypes,
            'offeredclass_today': offeredclass_today,
            'offeredclass_week': offeredclass_week,
            'offeredclass_month': offeredclass_month}
    return render(request, 'classes.html', json)


def getOffersPage(request):
    sunday = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday() + 1)
    all_offertypes = OfferType.objects.all()
    print(datetime.date.today().day)
    print(datetime.date.today().month)
    print(datetime.date.today())
    print(sunday)
    offer_today = Offer.objects.filter(created__day=datetime.date.today().day)
    offer_week = Offer.objects.filter(created__gte=sunday)
    offer_month = Offer.objects.filter(created__month=datetime.date.today().month)
    json = {'all_offertypes': all_offertypes,
            'offer_today': offer_today,
            'offer_week': offer_week,
            'offer_month': offer_month}
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
            print("form1 valid")
            newuser = form.save()
            errors = form.errorlist
            errors.update(dict(form.errors.items()))
            print(errors)

            current_site = get_current_site(request)
            subject = 'Activate your UnivHub Account.'
            message = render_to_string('password_change_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
                'token': account_activation_token.make_token(newuser),
            })
            # user.email_user(subject, message)
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            return JsonResponse(errors)
        else:
            print("form1 invalid")
            errors = form.errorlist
            print(errors)
            errors.update(dict(form.errors.items()))
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


@csrf_exempt
def jsonHandler(request: wsgi.WSGIRequest, action=None, operation=None):
    type = request.META.get('CONTENT_TYPE')

    try:
        # print the details
        print("Request on jsonHandler")
        print("Raw json data     :", request.body)
        print("Request parameters:", request.content_params)
        try:
            # try to convert body into json object
            json_data = json.loads(request.body.decode(encoding='UTF-8'))

            # if the request is from direct url
            if action is not None and operation is not None:
                json_data['action'] = {'data': action, 'operation': operation}
            return handler.handle_json(json_data)

        except Exception as e:
            # maybe the data is not json.
            # try other methods
            return JsonResponse({'status': "Error", "Reason": "Not a json data"})


    except Exception:
        # some other error in non json handling
        return JsonResponse({'status': "Error", "Reason": "Unknown error"})



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
        print(uid)

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
