from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django import forms
from sadmin.models import Consultancy
import json


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
