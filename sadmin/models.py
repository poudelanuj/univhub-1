# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class Header(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'header'


class Major(models.Model):
    major_name = models.CharField(max_length=250)

    class Meta:
        db_table = 'major'


class Ranking(models.Model):
    u = models.ForeignKey('Universities', models.DO_NOTHING, blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)
    ranking_type = models.CharField(max_length=7, blank=True, null=True)
    type_reference_table = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ranking'

class Document(models.Model):
    student=models.ForeignKey(User)
    name=models.CharField(max_length=25)
    DOCTYPE_CHOICES=(('a','first'),('b','second'),('c','third'),('d','fourth'))
    doctype=models.CharField(max_length=25,choices=DOCTYPE_CHOICES,help_text='Document Type')
    location=models.TextField()
    class Meta:
        db_table='Document'


class RequirementBySubject(models.Model):
    u = models.ForeignKey('Universities', models.DO_NOTHING)
    r_id = models.IntegerField()
    sub = models.ForeignKey('Requirements', models.DO_NOTHING)
    requirement_description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'requirement_by_subject'


class Requirements(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'requirements'


class SubHeader(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        db_table = 'sub_header'


class SubMajor(models.Model):
    major = models.ForeignKey(Major, models.DO_NOTHING, blank=True, null=True)
    sub_major_name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'sub_major'


class UniAddress(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250, blank=True, null=True)
    zip_code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'uni_address'


class UniAddressMapping(models.Model):
    u = models.ForeignKey('Universities', models.DO_NOTHING, blank=True, null=True)
    a = models.ForeignKey(UniAddress, models.DO_NOTHING, blank=True, null=True)
    is_main = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'uni_address_mapping'


class Universities(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    logo_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'universities'


class UniversityContent(models.Model):
    u = models.ForeignKey(Universities, models.DO_NOTHING)
    h = models.ForeignKey(Header, models.DO_NOTHING)
    sh = models.ForeignKey(SubHeader, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'university_content'


class UniversityRequirement(models.Model):
    u = models.ForeignKey(Universities, models.DO_NOTHING)
    r = models.ForeignKey(Requirements, models.DO_NOTHING, blank=True, null=True)
    requirement_for = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'university_requirement'


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    apply_for = models.CharField(max_length=255)
    dob = models.DateField()
    mobile = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)

    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:

        db_table = 'users'
class Notification(models.Model):
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    sender = models.ForeignKey(User,related_name='sender')
    read = models.BooleanField(default=False)
    title=models.CharField(blank=True,null=True,max_length=50)
    Type = models.IntegerField()
    message = models.TextField()
    created = models.DateTimeField()


    class Meta:

        db_table = 'notifications'

class AdminProfile(models.Model):
    consultancyName= models.CharField(max_length=30)
    pan_vat= models.CharField(max_length=20)
    reg_no= models.CharField(max_length=20)
    location= models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    phone = models.IntegerField()
    description = models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table="adminprofile"


class ModeratorProfile(models.Model):
    mobile = models.IntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)

    class Meta:
        db_table="moderatorprofile"


class CounselorProfile(models.Model):
    mobile = models.IntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name='userid')
    address = models.CharField(max_length=20)
    admin= models.ForeignKey(User,on_delete=models.CASCADE,default=None,related_name='adminid')

    class Meta:
        db_table = "counselorprofile"
