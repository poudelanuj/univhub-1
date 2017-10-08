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


class AdminProfile(models.Model):
    consultancyname = models.CharField(db_column='consultancyName', max_length=30)  # Field name made lowercase.
    pan_vat = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    phone = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_user_profile")

    class Meta:
        db_table = 'adminprofile'


class ApplyType(models.Model):
    applytype = models.CharField(max_length=15)

    class Meta:
        db_table = 'applytype'


class ClassType(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = 'classtype'

    def __str__(self):
        return self.title


class CounselorProfile(models.Model):
    mobile = models.IntegerField()
    address = models.CharField(max_length=20)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='adminid')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="counselor_user_profile")

    class Meta:
        db_table = 'counselor_profile'


class Country(models.Model):
    countryname = models.CharField(max_length=15)

    class Meta:
        db_table = 'country'


class Deliveryman(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)

    class Meta:
        db_table = 'deliveryman'


class District(models.Model):
    districtname = models.CharField(max_length=15)

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.districtname


class DocumentFor(models.Model):
    documentforname = models.CharField(max_length=30)

    class Meta:
        db_table = 'document_for'


class DocumentType(models.Model):
    name = models.CharField(max_length=30)
    documentfor = models.ForeignKey('DocumentFor', on_delete= None)

    class Meta:
        db_table = 'document_type'


class Header(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'header'


class Levels(models.Model):
    level_id = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'levels'


class Major(models.Model):
    major_name = models.CharField(max_length=250)

    class Meta:
        db_table = 'major'

    def __str__(self):
        return self.major_name


class ModeratorProfile(models.Model):
    mobile = models.IntegerField()
    address = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'moderator_profile'


class NotificationType(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    class Meta:
        db_table = 'notification_type'


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

    class Meta:
        db_table = 'notification'


class Offer(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    discountpercent = models.IntegerField(blank=True, null=True)
    scholarshippercent = models.IntegerField(blank=True, null=True)
    validity = models.DateField()
    created = models.DateTimeField()
    offerinclass = models.ForeignKey('OfferedClass', models.DO_NOTHING, blank=True, null=True)
    offertype = models.ForeignKey('OfferType', models.DO_NOTHING)
    university = models.ForeignKey('University', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'offer'

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

    class Meta:
        db_table = 'offered_class'

    def __str__(self):
        return self.name


class OfferType(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = 'offer_type'

    def __str__(self):
        return self.title


class Pickup(models.Model):
    pickup_date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=50)
    is_pending = models.IntegerField()
    created_date = models.DateField()
    document_for = models.ForeignKey('DocumentType', models.DO_NOTHING)

    pickup_of = models.ForeignKey(User, limit_choices_to={'groups__name': "studentGroup"}, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pickup'


class PickupDetail(models.Model):
    documentid = models.ForeignKey('UploadedDocument', models.DO_NOTHING)
    pickupid = models.ForeignKey(Pickup, models.DO_NOTHING)

    class Meta:
        db_table = 'pickup_detail'


class ProgramsOffered(models.Model):
    programoffered = models.CharField(max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'programs_offered'


class Ranking(models.Model):
    university = models.ForeignKey('University', models.DO_NOTHING, blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)
    ranking_type = models.CharField(max_length=7, blank=True, null=True)
    type_reference_table = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ranking'


class RegisteredClass(models.Model):
    offeredclass = models.ForeignKey(OfferedClass, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'registered_class'


class RegisteredOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'registered_offer'


class ReqMap(models.Model):
    hash_id = models.IntegerField(primary_key=True)
    u = models.ForeignKey('University', models.DO_NOTHING)
    level = models.ForeignKey(Levels, models.DO_NOTHING)
    submajor = models.ForeignKey('SubMajor', models.DO_NOTHING, blank=True, null=True)
    req = models.ForeignKey('SubReqByUniversity', models.DO_NOTHING)

    class Meta:
        db_table = 'req_map'


class Requirements(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'requirements'


class RequirementBySubject(models.Model):
    u = models.ForeignKey('University', models.DO_NOTHING)
    r_id = models.IntegerField()
    sub = models.ForeignKey('Requirements', models.DO_NOTHING)
    requirement_description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'requirement_by_subject'


class Scheduledpickup(models.Model):
    deliverydate = models.DateField()
    deliverytime = models.TimeField()
    is_picked = models.IntegerField(blank=True, null=True)
    deliveryman = models.ForeignKey(Deliveryman, models.DO_NOTHING)
    pickup = models.ForeignKey(Pickup, models.DO_NOTHING)

    class Meta:
        db_table = 'scheduled_pickup'


class SubHeader(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        db_table = 'sub_header'


class SubMajor(models.Model):
    major = models.ForeignKey('Major', models.DO_NOTHING)
    sub_major_name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'sub_major'

    def __str__(self):
        return self.sub_major_name


class SubReqByUniversity(models.Model):
    r_id = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sub_req_by_uni'


class Subjects(models.Model):
    sub_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    belongs_to = models.ForeignKey(SubMajor, models.DO_NOTHING, db_column='belongs_to')

    class Meta:
        db_table = 'subjects'


class Tutor(models.Model):
    name = models.CharField(max_length=200)
    qualification = models.TextField()

    class Meta:
        db_table = 'tutor'


class UniAddress(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250, blank=True, null=True)
    zip_code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'uni_address'


class UniAddressMapping(models.Model):
    u = models.ForeignKey('University', models.DO_NOTHING)
    a = models.ForeignKey(UniAddress, models.DO_NOTHING, blank=True, null=True)
    is_main = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'uni_address_mapping'


class University(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    logo_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'universities'

    def __str__(self):
        return self.name


class UniversityContent(models.Model):
    u = models.ForeignKey(University, models.DO_NOTHING)
    h = models.ForeignKey(Header, models.DO_NOTHING)
    sh = models.ForeignKey(SubHeader, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'university_content'


class UniversityRequirement(models.Model):
    u = models.ForeignKey(University, models.DO_NOTHING)
    r = models.ForeignKey(Requirements, models.DO_NOTHING)
    base_score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'university_requirement'


class UploadedDocument(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'groups__name': "studentGroup"}, on_delete=models.CASCADE)

    docname = models.CharField(max_length=30)
    url = models.TextField()
    doctype = models.ForeignKey('DocumentType')

    class Meta:
        db_table = 'uploaded_document'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dob = models.DateField()
    mobile = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    scholarship = models.IntegerField()
    citizenship = models.CharField(max_length=15)
    passport = models.CharField(max_length=15, blank=True, null=True)

    district = models.ForeignKey('District', models.DO_NOTHING)
    applied_country = models.ForeignKey('Country', models.DO_NOTHING)
    sub_major = models.ForeignKey('SubMajor', models.DO_NOTHING)
    apply_type = models.ForeignKey('ApplyType', models.DO_NOTHING, )
    program = models.ForeignKey('ProgramsOffered', models.DO_NOTHING)
    isblocked = models.BooleanField(default=False)
    class Meta:
        db_table = 'user_profile'


        # -----------------------------------------------------------------
        # -----------------------------------------------------------------
        # -----------------------------------------------------------------
        # -----------------------------------------------------------------
        # the table references for
