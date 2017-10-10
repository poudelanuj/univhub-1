import datetime

from django import forms
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

from .models import Student, Consultancy, ModeratorProfile, Counselor, Country


class AddAdminForm(forms.Form):
    username = forms.CharField(max_length=25)
    consultancyName = forms.CharField(max_length=30)
    pan_vat = forms.CharField(max_length=20)
    reg_no = forms.CharField(max_length=20)
    location = forms.CharField(max_length=20)
    website = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    errorlist = {}

    def clean(self):
        cleaned_data = super(AddAdminForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')
        password2 = cleaned_data.get('password2')
        if username in User.objects.all().values_list('username', flat=True):
            self.errorlist['username'] = 'This username already exists'
            raise forms.ValidationError("This username already exists")

        return cleaned_data

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            first_name="admin",
                                            last_name="admin",
                                            password=self.cleaned_data['password'],
                                            email=self.cleaned_data['email'],
                                            date_joined=datetime.datetime.today(),
                                            is_superuser=False,
                                            is_staff=False,
                                            )
        m1 = Consultancy(user=new_user, consultancyName=self.cleaned_data.get('consultancyName'),
                         pan_vat=self.cleaned_data.get('pan_vat'),
                         reg_no=self.cleaned_data.get('reg_no'),
                         location=self.cleaned_data.get('location'),
                         website=self.cleaned_data.get('website'),
                         phone=self.cleaned_data.get('phone'),
                         company_logo=self.cleaned_data.get('image'),
                         description=self.cleaned_data.get('description'))

        m1.save()
        admingroup = get_object_or_404(Group, name="adminGroup")
        admingroup.user_set.add(new_user)
        return new_user


class AddModeratorForm(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=200, help_text='Required')
    location = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    errorlist = {}

    def clean(self):
        cleaned_data = super(AddModeratorForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        location = cleaned_data.get('location')

        if username in User.objects.all().values_list('username', flat=True):
            self.errorlist['username'] = 'This username already exists'
            raise forms.ValidationError("This username already exists")
        if email in User.objects.all().values_list('email', flat=True):
            self.errorlist['email'] = 'This email already exists'
            raise forms.ValidationError("This email already exists")
        if password != password2:
            self.errorlist['password'] = 'The two password fields must match. Got it!!??'
            raise forms.ValidationError("The two password fields must match. Got it!!??")

        return cleaned_data

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            first_name="moderator",
                                            last_name="moderator",
                                            password=self.cleaned_data['password'],
                                            email=self.cleaned_data['email'],
                                            date_joined=datetime.datetime.today(),
                                            is_superuser=False,
                                            is_staff=False,
                                            )
        m1 = ModeratorProfile(user=new_user, mobile=00000000,
                              address=self.cleaned_data['location'], profile_image=self.cleaned_data['image'], )
        m1.save()
        moderatorgroup = get_object_or_404(Group, name="moderatorGroup")
        moderatorgroup.user_set.add(new_user)
        return new_user


class AddCounselorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super(AddCounselorForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=25)
    address = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    errorlist = {}

    def clean(self):
        cleaned_data = super(AddCounselorForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        address = cleaned_data.get('address')
        if username in User.objects.all().values_list('username', flat=True):
            self.errorlist['username'] = 'This username already exists'
            raise forms.ValidationError("This username already exists")

        if password != password2:
            self.errorlist['password'] = 'The two password fields must match. Got it!!??'
            raise forms.ValidationError("The two password fields must match. Got it!!??")

        return cleaned_data

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            first_name="counselor",
                                            last_name="counselor",
                                            password=self.cleaned_data['password'],
                                            email=self.cleaned_data['email'],
                                            date_joined=datetime.datetime.today(),
                                            is_staff=False,
                                            is_superuser=False,
                                            )
        m1 = Counselor(user=new_user, mobile=00,
                       address=self.cleaned_data.get('address'),
                       profile_image=self.cleaned_data['image'],
                       admin=self.user)
        m1.save()
        counselorgroup = get_object_or_404(Group, name="counsellorGroup")
        counselorgroup.user_set.add(new_user)
        return new_user


class SignupForm(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Confirm Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text="Confirm Password")
    dob = forms.DateField(required=False)
    apply_for = forms.CharField()
    mobile = forms.CharField()

    def clean(self):

        cleaned_data = super(SignupForm, self).clean()
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
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            first_name=self.cleaned_data['first_name'],
                                            last_name=self.cleaned_data['last_name'],
                                            password=self.cleaned_data['password'],
                                            email=self.cleaned_data['email'],
                                            is_superuser=False,
                                            is_active=False,
                                            )
        country=get_object_or_404(Country,countryname=self.cleaned_data.get('apply_for'))
        m1 = Student(user=new_user, mobile=self.cleaned_data.get('mobile'),

                     dob=self.cleaned_data.get('dob'),
                     apply_for=Country)
        m1.save()
        return new_user
