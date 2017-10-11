import datetime

from django import forms
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404


class StudentEditForm(forms.Form):
    errorlist = {}
    email = forms.EmailField(max_length=200, help_text='Required',required=False)
    firstname = forms.CharField(max_length=25,required=False)
    middlename = forms.CharField(max_length=25,required=False)
    lastname = forms.CharField(max_length=25,required=False)
    gender = forms.CharField(max_length=10,required=False)
    dobnp = forms.DateField(required=False)
    doben = forms.DateField(required=False)
    phone1=forms.CharField(max_length=25,required=False)
    phone2=forms.CharField(max_length=25,required=False)
    phone3=forms.CharField(max_length=25,required=False)
    addressline1=forms.CharField(max_length=25,required=False)
    addressline2=forms.CharField(max_length=25,required=False)
    addressline3=forms.CharField(max_length=25,required=False)
    district = forms.CharField(max_length=25,required=False)
    city = forms.CharField(max_length=25,required=False)
    permaddressline1=forms.CharField(max_length=25,required=False)
    permaddressline2=forms.CharField(max_length=25,required=False)
    permaddressline3=forms.CharField(max_length=25,required=False)
    permdistrict = forms.CharField(max_length=25,required=False)
    permcity = forms.CharField(max_length=25,required=False)

    def clean(self):
        cleaned_data = super(StudentEditForm, self).clean()
        email = cleaned_data.get('email')
        if email in User.objects.all().values_list('email', flat=True):
            self.errorlist['username'] = 'This email already exists'
        print(email)
        print(cleaned_data.get('first_name'))
        print("hey bro")
        return cleaned_data

