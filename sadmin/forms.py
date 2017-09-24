from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User
import django.contrib.auth.password_validation as validators
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,AdminProfile, ModeratorProfile, CounselorProfile


class AddAdminForm(ModelForm):
    consultancyName= forms.CharField(max_length=30)
    pan_vat= forms.CharField(max_length=20)
    reg_no= forms.CharField(max_length=20)
    location= forms.CharField(max_length=20)
    website = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    errorlist={}

    def clean(self):
        cleaned_data=super(AddAdminForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')

        if username in User.objects.all().values_list('username', flat=True):
            self.errorlist['username']='This username already exists'
            raise forms.ValidationError("This username already exists")
        if email in User.objects.all().values_list('email', flat=True):
            raise forms.ValidationError("This email already exists")
        if password != password2:
            raise forms.ValidationError("The two password fields must match. Got it!!??")
        return cleaned_data

    def save(self):
        new_user=User.objects.create_user(username=self.cleaned_data['username'],
                                    first_name="admin",
                                    last_name="admin",
                                    password=self.cleaned_data['password'],
                                    email=self.cleaned_data['email'],
                                    is_superuser=False,
                                    is_staff=False,
                                        )
        m1=AdminProfile(user=new_user, consultancyName=self.cleaned_data.get('consultancyName'),
                            pan_vat=self.cleaned_data.get('pan_vat'),
                            reg_no=self.cleaned_data.get('reg_no'),
                            location=self.cleaned_data.get('location'),
                            website=self.cleaned_data.get('website'),
                            phone=self.cleaned_data.get('phone'),
                            description=self.cleaned_data.get('description'))
        m1.save()
        return new_user

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')


class AddModeratorForm(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=200, help_text='Required')
    location=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    errorlist={}
    def clean(self):
        cleaned_data=super(AddModeratorForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        location = cleaned_data.get('location')
        print(username)
        print(email)
        print(password)
        print(password2)
        print(location)

        if username in User.objects.all().values_list('username', flat=True):
            self.errorlist['username']='This username already exists'
            raise forms.ValidationError("This username already exists")
        if email in User.objects.all().values_list('email', flat=True):
            self.errorlist['email']='This email already exists'
            raise forms.ValidationError("This email already exists")
        if password != password2:
            self.errorlist['password']='The two password fields must match. Got it!!??'
            raise forms.ValidationError("The two password fields must match. Got it!!??")

        return cleaned_data

    def save(self):
        new_user=User.objects.create_user(username=self.cleaned_data['username'],
                                    first_name="no",
                                    last_name="non",
                                    password=self.cleaned_data['password'],
                                    email=self.cleaned_data['email'],
                                    is_superuser=False,
                                    is_staff=False,
                                        )
        m1=ModeratorProfile(user=new_user, mobile=00000000,
            address=self.cleaned_data['location'])
        m1.save()
        return new_user




# class AddCounselorForm(ModelForm):
#     mobile = forms.IntegerField()
#     address = forms.CharField(max_length=20)
#     admin = forms.

#     def clean(self):
#         cleaned_data=super(AddCounselorForm, self).clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#         email = cleaned_data.get('email')

#         validators.validate_password(password=password,user=username)
#         if email in User.objects.all().values_list('email', flat=True):
#             raise forms.ValidationError("This email already exists")
#         # if password != password2:
#         #     raise forms.ValidationError("The two password fields must match. Got it!!??")
#         return cleaned_data

#     def save(self):
#         new_user=User.objects.create_user(username=self.cleaned_data['username'],
#                                     first_name=self.cleaned_data['first_name'],
#                                     last_name=self.cleaned_data['last_name'],
#                                     password=self.cleaned_data['password'],
#                                     email=self.cleaned_data['email'],
#                                     )
#         m1=CounselorProfile(user=new_user, mobile=self.cleaned_data.get('mobile'),
#                          address=self.cleaned_data.get('address'),
#                          admin = self.cleaned_data.get('admin'))
#         m1.save()
#         return new_user

#     class Meta:
#         model = User
#         fields = ('first_name','last_name','username','email','password','is_superuser')
class SignupForm(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name=forms.CharField(max_length=25)
    last_name=forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput(),help_text="Confirm Password")
    password2 = forms.CharField(widget=forms.PasswordInput(),help_text="Confirm Password")
    dob=forms.DateField(required=False)
    apply_for=forms.CharField()
    mobile=forms.CharField()
    def clean(self):

        cleaned_data=super(SignupForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        if username in User.objects.all().values_list('username', flat=True):
            raise forms.ValidationError("This username already exists")
        if email in User.objects.all().values_list('email', flat=True):
            raise forms.ValidationError("This email already exists")
        if password != password2:
            raise forms.ValidationError("The two password fields must match. Got it!!??")

        return cleaned_data
    def save(self):
         # create new user
        new_user=User.objects.create_user(username=self.cleaned_data['username'],
                                    first_name=self.cleaned_data['first_name'],
                                    last_name=self.cleaned_data['last_name'],
                                    password=self.cleaned_data['password'],
                                    email=self.cleaned_data['email'],
                                    is_superuser=False,
                                    is_active=False,
                                        )
        m1=UserProfile(user=new_user,mobile=self.cleaned_data.get('mobile'),
                        dob=datetime.date.today(),
                        apply_for=self.cleaned_data.get('apply_for'))
        m1.save()
        return new_user
