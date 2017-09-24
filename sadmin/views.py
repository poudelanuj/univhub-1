from django.shortcuts import render
from notifications.signals import notify
# Create your views here.
from django.shortcuts import get_object_or_404
from .models import Document,Notification
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from .forms import SignupForm,AddModeratorForm,AddAdminForm,AddCounselorForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token

def index(request):
    return render(request, "admin-dashboard.html")

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
    data={'notifycount':Notification.objects.filter(receiver=user).count()}
    return JsonResponse(data)
def getNotificationslist(request):

    notifications=Notification.objects.filter(receiver=request.user).order_by('-created')

    html = render_to_string('notification_drop.html', {'notifications': notifications})

    return HttpResponse(html)
def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()

            current_site = get_current_site(request)
            subject = 'Activate your UnivHub Account.'
            message = render_to_string('acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
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
        m1=UserProfile(user=user)
        m1.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def addadmin(request):
    form = AddAdminForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            errors=form.errorlist
            print(errors)
            return JsonResponse(errors)
        else:
            errors=form.errorlist
            print(errors)
            return JsonResponse(errors)

    return JsonResponse(errors)

def addmoderator(request):
    form = AddModeratorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            errors=form.errorlist
            print(errors)
            return JsonResponse(errors)
        else:
            errors=form.errorlist
            print(errors)
            return JsonResponse(errors)


    return JsonResponse(errors)

def addcounselor(request):
    user=request.user
    form = AddCounselorForm(request.POST,user=user or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            errors=form.errorlist
            print(errors)
            return JsonResponse(errors)
        else:
            errors=form.errorlist
            print(errors)
            return JsonResponse(errors)


    return JsonResponse(errors)
