# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib import admin

from django.db import models
from django.contrib.auth.models import User
from university.models import *
from student.models import *


class Consultancy(User):
    consultancyname = models.CharField(db_column='consultancyName', max_length=30)  # Field name made lowercase.
    pan_vat = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    phone = models.IntegerField()
    description = models.TextField()
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.consultancyname


class ApplyType(models.Model):
    applytype = models.CharField(max_length=15)

    def __str__(self):
        return self.applytype


class ClassType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Counselor(User):
    mobile = models.IntegerField()
    address = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="counselor_user_profile")
    is_blocked = models.BooleanField(default=False)


class Country(models.Model):
    countryname = models.CharField(max_length=15)

    def __str__(self):
        return self.countryname


class Deliveryman(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)


class District(models.Model):
    districtname = models.CharField(max_length=15)

    def __str__(self):
        return self.districtname


class DocumentFor(models.Model):
    documentforname = models.CharField(max_length=30)


class DocumentType(models.Model):
    name = models.CharField(max_length=30)
    documentfor = models.ForeignKey('DocumentFor', on_delete=None)


class ModeratorProfile(User):
    mobile = models.IntegerField()
    address = models.CharField(max_length=20)
    is_blocked = models.BooleanField(default=False)


class NotificationType(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)


class Notification(models.Model):
    read = models.IntegerField()
    title = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey('NotificationType', models.DO_NOTHING)
    message = models.TextField()
    created = models.DateTimeField()
    map_url = models.TextField(blank=True, null=True)
    web_url = models.TextField(blank=True, null=True)
    receiver = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='pk_not_receiver')
    sender = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='pk_not_sender')


class Offer(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    discountpercent = models.IntegerField(blank=True, null=True)
    scholarshippercent = models.IntegerField(blank=True, null=True)
    validity = models.DateField()
    created = models.DateTimeField()
    offerinclass = models.ForeignKey('OfferedClass', models.DO_NOTHING, blank=True, null=True)
    offertype = models.ForeignKey('OfferType', models.DO_NOTHING)
    university = models.ForeignKey(University, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.title


class OfferedClass(models.Model):
    name = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    price = models.IntegerField()
    discountpercent = models.IntegerField()
    location = models.CharField(max_length=100)
    starttime = models.TimeField()
    endtime = models.TimeField()
    created = models.DateTimeField()
    classtype = models.ForeignKey(ClassType, models.DO_NOTHING)
    tutor = models.ForeignKey('Tutor', models.DO_NOTHING)

    def __str__(self):
        return self.name


class OfferType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Pickup(models.Model):
    pickup_date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
    is_pending = models.IntegerField()
    created_date = models.DateField()
    document_for = models.ForeignKey('DocumentType', models.DO_NOTHING)

    pickup_of = models.ForeignKey(User, limit_choices_to={'groups__name': "studentGroup"}, on_delete=models.CASCADE)


class PickupDetail(models.Model):
    documentid = models.ForeignKey('UploadedDocument', models.DO_NOTHING)
    pickupid = models.ForeignKey(Pickup, models.DO_NOTHING)


class RegisteredClass(models.Model):
    offeredclass = models.ForeignKey(OfferedClass, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class RegisteredOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)


class Scheduledpickup(models.Model):
    deliverydate = models.DateField()
    deliverytime = models.TimeField()
    is_picked = models.IntegerField(blank=True, null=True)
    deliveryman = models.ForeignKey(Deliveryman, models.DO_NOTHING)
    pickup = models.ForeignKey(Pickup, models.DO_NOTHING)


class Tutor(models.Model):
    name = models.CharField(max_length=200)
    qualification = models.TextField()


class UploadedDocument(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'groups__name': "studentGroup"}, on_delete=models.CASCADE)

    docname = models.CharField(max_length=30)
    url = models.TextField()
    doctype = models.ForeignKey('DocumentType')


identification = (
    ('Passport', 'Passport'),
    ('Citizenship', 'Citizenship')
)


class Sponsor(User):
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    relationship = models.CharField(max_length=20)
    identification = models.CharField(choices=identification, max_length=15)
    fileurl = models.TextField()
    phone1 = models.CharField(max_length=15, blank=True, null=True)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    phone3 = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.middle_name + " : " + self.relationship


class Address(models.Model):
    district = models.ForeignKey('District', models.DO_NOTHING)
    city = models.CharField(max_length=20)
    AddressLine1 = models.CharField(max_length=20)
    AddressLine2 = models.CharField(max_length=20)
    AddressLine3 = models.CharField(max_length=20)

    def __str__(self):
        return self.district + " : " + self.city


gender = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Student(User):
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(choices=gender, max_length=6)
    dob_np = models.DateField()
    dob_en = models.DateField()
    phone1 = models.CharField(max_length=15, blank=True, null=True)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    phone3 = models.CharField(max_length=15, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    scholarship = models.IntegerField()
    citizenship = models.CharField(max_length=15)
    passport = models.CharField(max_length=15, blank=True, null=True)
    applied_country = models.ForeignKey(Country, models.DO_NOTHING)
    sub_major = models.ForeignKey(SubMajor, models.DO_NOTHING)
    apply_type = models.ForeignKey('ApplyType', models.DO_NOTHING, )
    program = models.ForeignKey(ProgramsOffered, models.DO_NOTHING)
    isblocked = models.BooleanField(default=False)
    student_consultancy = models.ForeignKey(Consultancy, models.DO_NOTHING, blank=True, null=True,
                                            related_name="consultancy_student")
    temp_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name="temp_address")
    perm_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True,
                                     related_name="perm_address")

    def __str__(self):
        return ("profile of " + str(self.user))

