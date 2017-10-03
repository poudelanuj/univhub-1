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
import datetime

# (what to be entered, what to be shown)
statusTypes = {
    ('Pending', 'Pending'),
    ('Scheduled', 'Scheduled'),
    ('Picked', 'Picked'),
    ('Unpicked', 'Unpicked'),
}


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


class District(models.Model):  # location of students
    districtname = models.CharField(max_length=15)

    class Meta:
        db_table = "district"


class Country(models.Model):  # available country for which students can apply
    countryname = models.CharField(max_length=15)

    class Meta:
        db_table = "country"


class ApplyType(models.Model):  # student apply or dependendent apply ?
    applytype = models.CharField(max_length=15)

    class Meta:
        db_table = "applytype"


class ProgramsOffered(models.Model):  # bachelor, masters, phd or diploma
    programOffered = models.CharField(max_length=20)

    class Meta:
        db_table = "programsOffered"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dob = models.DateField()
    mobile = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    scholarship = models.BooleanField()  # apply for scholarship or not ?
    citizenship = models.CharField(max_length=15)
    passport = models.CharField(max_length=15, blank=True, null=True)

    district = models.ForeignKey(District, models.DO_NOTHING)
    apply_for = models.ForeignKey(Country, models.DO_NOTHING)
    sub_major = models.ForeignKey(SubMajor, models.DO_NOTHING)
    apply_type = models.ForeignKey(ApplyType, models.DO_NOTHING, )
    program = models.ForeignKey(ProgramsOffered, models.DO_NOTHING)

    class Meta:
        db_table = 'user_profile'


class Notification(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver',blank=True, null=True)
    sender = models.ForeignKey(User, related_name='sender')
    read = models.BooleanField(default=False)
    title = models.CharField(blank=True, null=True, max_length=50)
    Type = models.IntegerField(blank=True,null=True)
    message = models.TextField()
    created = models.DateTimeField()

    class Meta:
        db_table = 'notifications'


class AdminProfile(models.Model):
    consultancyName = models.CharField(max_length=30)
    pan_vat = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    phone = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = "adminprofile"


class ModeratorProfile(models.Model):
    mobile = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)

    class Meta:
        db_table = "moderatorprofile"


class CounselorProfile(models.Model):
    mobile = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userid')
    address = models.CharField(max_length=20)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='adminid')

    class Meta:
        db_table = "counselorprofile"


class documenttype(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'documenttype'

    def __str__(self):
        return self.name


class uploadeddocuments(models.Model):
    student_id = models.ForeignKey(User, limit_choices_to={'groups__name': "studentGroup"}, on_delete=models.CASCADE)
    doctype = models.ForeignKey(documenttype)
    docname = models.CharField(max_length=30)
    url = models.CharField(max_length=250)

    class Meta:
        db_table = 'uploadeddocuments'

    def __str__(self):
        return str(self.student_id) + " : " + str(self.docname)


class pickup(models.Model):
    pickupof = models.ForeignKey(User, limit_choices_to={'groups__name': "studentGroup"}, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=9, choices=statusTypes, default='Pending')

    class Meta:
        db_table = 'pickup'

    def __str__(self):
        return str(self.pickupof.username)


class pickupdetails(models.Model):
    pickupid = models.ForeignKey(pickup, on_delete=models.CASCADE)
    documentid = models.ForeignKey(uploadeddocuments, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pickupdetails'

    def __str__(self):
        return str(self.pickupid) + str(self.documentid)


class Tutor(models.Model):
    name = models.CharField(max_length=200)
    qualification = models.TextField()

    class Meta:
        db_table='tutor'

    def __str__(self):
        return self.name


class ClassType(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table='classtype'

    def __str__(self):
        return self.title


class OfferedClass(models.Model):
    name = models.CharField(max_length=100)
    classtype = models.ForeignKey(ClassType, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    discountpercent = models.IntegerField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    scholarshippercent = models.IntegerField()
    location = models.CharField(max_length=100)
    starttime = models.TimeField()
    endtime = models.TimeField()
    created = models.DateTimeField(default= datetime.datetime.now())

    class Meta:
        db_table='offeredclass'

    def __str__(self):
        return self.name


class RegisteredClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offeredclass = models.ForeignKey(OfferedClass, on_delete=models.CASCADE)

    class Meta:
        db_table='registeredclass'


class OfferType(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table='offertype'

    def __str__(self):
        return self.title


class Offer(models.Model):
    title =  models.CharField(max_length=50)
    description = models.TextField()
    offertype = models.ForeignKey(OfferType, on_delete=models.CASCADE)
    offerinclass = models.ForeignKey(OfferedClass, on_delete=models.CASCADE, blank=True, null=True)
    discountpercent = models.IntegerField(null=True, blank=True)
    university = models.ForeignKey(Universities, on_delete=models.CASCADE, blank=True, null=True)
    scholarshippercent = models.IntegerField(null=True, blank=True)
    validity = models.DateField()
    created = models.DateTimeField(default= datetime.datetime.now())

    class Meta:
        db_table='offer'

    def __str__(self):
        return self.title