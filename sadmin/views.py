import json

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
from django.views.decorators.csrf import csrf_exempt

from json_requests import handler
# Create your views here.
from .forms import SignupForm, AddModeratorForm, AddAdminForm, AddCounselorForm
from .models import *
from .tokens import account_activation_token
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import datetime
from django.contrib.auth.models import User, Group
import traceback

from django.contrib.auth.decorators import login_required


# from fcm_django.models import FCMDevice

@login_required
def index(request):
    user = request.user
    group = user.groups.all()[0]
    if group.name == 'univhub_super_admin' or group.name == 'univhub_moderator':
        return render(request, 'admin-dashboard.html',
                      {'adminGroup': User.objects.filter(groups__name='consultancy_admin'),
                       'moderatorGroup': User.objects.filter(groups__name='univhub_moderator'),
                       'counsellorGroup': User.objects.filter(groups__name='consultancy_moderator'),
                       'studentCount': User.objects.filter(groups__name='student').count(),
                       'todayjoined': User.objects.filter(date_joined__day=datetime.now().day,
                                                          groups__name='studentGroup').count()
                       })
    elif group == 'student':
        pass
    else:
        return render(request, 'consultancy_dashboard.html',
                      {
                          'counsellorGroup': Counselor.objects.filter(consultancy__pk=user.pk),
                          'studentCount': Student.objects.filter(consultancy=user.pk).count(),
                          'todayjoined': Student.objects.filter(user__date_joined__day=datetime.now().day,
                                                                consultancy=user.pk).count()
                      })


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


def showdocumentuploadtest(request):
    return render(request, 'documentupload.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        m = Student(user=user)
        m1.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def getStudentslistPage(request):
    students = User.objects.filter(groups__name="studentGroup")
    return render(request, 'students-list.html', {'students': students})

    # all_students = User.objects.filter(groups=4)
    # paginator = Paginator(all_students, 10)
    # page = request.GET.get('page', 1)  # get page or 1
    # try:
    #     students = paginator.page(page)
    #     print(students)
    # except PageNotAnInteger:  # if page is not an integer
    #     students = paginator.page(1)
    #     print("page not an integer")
    # except EmptyPage:  # if the page number goes out of bound
    #     students = paginator.page(paginator.num_pages)
    # print(students)
    # return render(request, 'students-list.html')


def addadmin(request):
    form = AddAdminForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            newuser = form.save()
            print("add here")
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
            print("form invalid")
            errors = form.errorlist
            errors.update(dict(form.errors.items()))
            print(errors)
            return JsonResponse(errors)

    return JsonResponse({'success'"False"})


def addmoderator(request):
    form = AddModeratorForm(request.POST, request.FILES or None)
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
    return JsonResponse({'success': False})


# todo
# remove change is_pending to False once the pickup is marked as scheduled.

def getPickupPage(request):
    now = datetime.now()
    sunday = datetime(now.year, now.month, now.day - now.weekday() - 1)

    pending_pickups = Pickup.objects.filter(is_pending=True)  # all pending pickups
    pending_documents = PickupDetail.objects.filter(pickupid__in=pending_pickups)  # all documents of pending
    nonpending_pickups = Pickup.objects.filter(is_pending=False)
    nonpending_documents = PickupDetail.objects.filter(pickupid__in=nonpending_pickups)

    today_pickups = pending_pickups.filter(created_date__day=datetime.now().day)
    week_pickups = pending_pickups.filter(created_date__gte=sunday)
    month_pickups = pending_pickups.filter(created_date__month=datetime.now().month)

    scheduled_pickup = Scheduledpickup.objects.exclude(is_picked=True).exclude(is_picked=False)
    today_schedule = scheduled_pickup.filter(deliverydate__day=datetime.now().day)
    week_schedule = scheduled_pickup.filter(deliverydate__gte=sunday)
    month_schedule = scheduled_pickup.filter(deliverydate__month=datetime.now().month)

    picked = Scheduledpickup.objects.filter(is_picked=1)
    today_picked = picked.filter(deliverydate__day=datetime.now().day)
    week_picked = picked.filter(deliverydate__gte=sunday)
    month_picked = picked.filter(deliverydate__month=datetime.now().month)

    unpicked = Scheduledpickup.objects.filter(is_picked=0)
    today_unpicked = unpicked.filter(deliverydate__day=datetime.now().day)
    week_unpicked = unpicked.filter(deliverydate__gte=sunday)
    month_unpicked = unpicked.filter(deliverydate__month=datetime.now().month)

    delivery_man = Deliveryman.objects.all()

    json = {'pending_documents': pending_documents, 'nonpending_documents': nonpending_documents,
            'today_pickups': today_pickups, 'week_pickups': week_pickups, 'month_pickups': month_pickups,
            'today_schedule': today_schedule, 'week_schedule': week_schedule, 'month_schedule': month_schedule,
            'today_picked': today_picked, 'week_picked': week_picked, 'month_picked': month_picked,
            'today_unpicked': today_unpicked, 'week_unpicked': week_unpicked, 'month_unpicked': month_unpicked,
            'delivery_man': delivery_man
            }

    return render(request, 'pickup.html', json)


def getClassesPage(request):
    now = datetime.now()
    sunday = datetime(now.year, now.month, now.day - now.weekday() - 1)
    all_classtypes = ClassType.objects.all()
    offeredclass_today = OfferedClass.objects.filter(created__day=datetime.now().day)
    offeredclass_week = OfferedClass.objects.filter(created__gte=sunday)
    offeredclass_month = OfferedClass.objects.filter(created__month=datetime.now().month)
    json = {'all_classtypes': all_classtypes,
            'offeredclass_today': offeredclass_today,
            'offeredclass_week': offeredclass_week,
            'offeredclass_month': offeredclass_month}
    return render(request, 'classes.html', json)


def getOffersPage(request):
    now = datetime.now()
    sunday = datetime(now.year, now.month, now.day - now.weekday() - 1)
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
    return render(request, 'student-profile.html', {'student': student})


# ajax calls handling part

def addcounselor(request):
    user = request.user
    form = AddCounselorForm(request.FILES, request.POST, user=user or None)
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
            print("form1 invalid")
            errors = form.errorlist
            errors.update(dict(form.errors.items()))
            return JsonResponse(errors)

    return JsonResponse({'success': False})


#delete role will cause the name not to appear in the list
def ajaxCallForDeleteRole(request):
    userId = request.GET.get('userId')
    usr = User.objects.get(id=userId)
    usr.is_active = False


    mygroup = Consultancy.objects.filter(user=userId)
    if(len(mygroup)):
        mygroup[0].is_blocked = True
        mygroup[0].save()

    mygroup = Counselor.objects.filter(user=userId)
    if (len(mygroup)):
        mygroup[0].is_blocked = True
        mygroup[0].save()

    mygroup = ModeratorProfile.objects.filter(user=userId)
    if (len(mygroup)):
        mygroup[0].is_blocked = True
        mygroup[0].save()

    data = informationCenter()
    reloadPortion = render_to_string('dashboard_admins_Info.html', data)
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
    reloadPortion = render_to_string('dashboard_admins_Info.html', data)
    return HttpResponse(reloadPortion)


def ajaxRemovePickupDocument(request):
    print("check")
    docId = request.GET.get('documentID')
    print("document to delete : " + docId)
    print(PickupDetail.objects.filter(documentid=docId))
    PickupDetail.objects.filter(id=docId).delete()
    return 1


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
