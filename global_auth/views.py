from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage

from django.views import View
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django import forms
from sadmin.models import Consultancy
import json

from sadmin.tokens import account_activation_token

def resetpassword(request):
    print("check reset")
    user = request.user
    if request.method == 'POST':
        print("processing your email reset...")
        myemail = request.POST.get('email')
        try:
            user = User.objects.get(email=myemail)
            print(user)
        except:
            return JsonResponse({'success':False, 'error':'User do not exist'})

        current_site = get_current_site(request)
        subject = "Reset Password"
        message = render_to_string('password_change_email.html',
                                    {'user':user, 'domain':current_site.domain,
                                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                    'token':account_activation_token.make_token(user)
                                    }
                                   )
        email = EmailMessage(subject,message,to=[myemail])
        email.send()
        return JsonResponse({'success':True, 'message': 'Check Your Email for reseting password.'})

    else:
        return render(request, 'forgetpassword.html')



class LoginView(FormView):
    class LoginForm(forms.Form):
        uname = forms.CharField()
        passwd = forms.CharField()
        submit_action = forms.CharField()

    def validate(self):
        return True

    loginForm = LoginForm
    initial = {'key': 'value'}
    template_name = 'auth_login_form.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous():
            return redirect('/sadmin/admin-dashboard.html')
        return render(request, 'auth_login_form.html')

    def post(self, request, *args, **kwargs):

        content_type = request.META.get('CONTENT_TYPE')
        print(content_type)
        if content_type == 'application/json':
            print("Json income")
            data = json.loads(request.body.decode(encoding='UTF-8'))
        else:
            data = QueryDict(request.body, encoding='UTF-8')
            for dat in data:
                if type(data[dat]) is list:
                    data[dat] = data[dat][0]

        user = authenticate(username=data['uname'], password=data['passwd'])

        if user is None:
            if content_type == 'application/json':
                print("json response")
                response = JsonResponse({'success': False, 'cause': "Invalid Login details"})
                response.status_code = 401
                return response
            else:
                return redirect('/login.django')
        else:
            login(request,user)
            print("session created")
            print(user, type(user))
           # print(user.sessions,type(user.sessions))
            if content_type == 'application/json':
                print("json response")
                return JsonResponse({'success': True, 'home': '/sadmin/admin-dashboard.html'})
            else:
                return redirect('/sadmin/admin-dashboard.html');


