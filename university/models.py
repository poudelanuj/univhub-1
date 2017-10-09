from django.db import models

# Create your models here.
class UniversityRequirement(models.Model):
    university = models.ForeignKey('University', models.DO_NOTHING)
    requirement = models.ForeignKey('Requirements', models.DO_NOTHING)
    base_score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'university_requirement'


class UniAddress(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250, blank=True, null=True)
    zip_code = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        db_table = 'uni_address'


class UniAddressMapping(models.Model):
    university = models.ForeignKey('University', models.DO_NOTHING)
    address = models.ForeignKey('UniAddress', models.DO_NOTHING, blank=True, null=True)
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
    university = models.ForeignKey('University', models.DO_NOTHING)
    header = models.ForeignKey('Header', models.DO_NOTHING)
    sub_header = models.ForeignKey('SubHeader', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'university_content'


class Header(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        db_table = 'header'


class Levels(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'levels'


class Major(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        db_table = 'major'

    def __str__(self):
        return self.major_name


class ReqMap(models.Model):
    hash_id = models.IntegerField(primary_key=True)
    u = models.ForeignKey('University', models.DO_NOTHING)
    level = models.ForeignKey('Levels', models.DO_NOTHING)
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
    belongs_to = models.ForeignKey('SubMajor', models.DO_NOTHING, db_column='belongs_to')

    class Meta:
        db_table = 'subjects'


class ProgramsOffered(models.Model):
    programoffered = models.CharField(max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'programs_offered'

    def __str__(self):
        return self.programoffered
class Ranking(models.Model):
    university = models.ForeignKey('University', models.DO_NOTHING, blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)
    ranking_type = models.CharField(max_length=7, blank=True, null=True)
    type_reference_table = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ranking'

class SubHeader(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        db_table = 'sub_header'