from django.db import models


class ListText(models.Model):
    content = models.TextField(null=True, blank=True, default=None)


class TitleText(models.Model):
    name = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.name


# Create your models here.
class UniversityRequirement(models.Model):
    university = models.ForeignKey('University', models.DO_NOTHING)
    requirement = models.ForeignKey('Requirement', models.DO_NOTHING)
    base_score = models.IntegerField(blank=True, null=True, default=None)


class UniversityAddress(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    university = models.ForeignKey('University', models.DO_NOTHING)
    is_main = models.BooleanField(blank=False, null=False)


class HighlightText(models.Model):
    university = models.ForeignKey("University")
    content = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return self.content


class University(models.Model):
    main_line = models.TextField(blank=True, null=True, default=None)
    name = models.CharField(max_length=250, blank=True, null=True)
    logo_url = models.CharField(max_length=1000, blank=True, null=True)
    web_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def highlights(self):
        highlights = []
        _highlights = HighlightText.objects.filter(university=self)
        # append the highlights
        for highlight in _highlights:
            highlights.append(highlight.content)
        return highlights

    def get_world_ranking(self):
        rank = Ranking.objects.filter(university=self,
                                      ranking_type=RankingType.objects.get_or_create(content="World")[0])
        if len(rank):
            return rank[0].ranking
        return None

    def description(self):
        return Detail.objects.filter(university=self)


class Detail(models.Model):
    university = models.ForeignKey("University")
    header = models.ForeignKey(TitleText, models.DO_NOTHING, blank=False, null=False, related_name="header")
    sub_header = models.ForeignKey(TitleText, models.DO_NOTHING, blank=True, null=True, related_name="sub_header")
    description = models.TextField(blank=True, null=True)


class Header(models.Model):
    content = models.TextField(blank=True, null=True, default=None)


class Level(models.Model):
    name = models.TextField(blank=True, null=True, default=None)


class Major(models.Model):
    name = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Dates(models.Model):
    date = models.TextField(blank=True, null=True, default=None)


class UniversitySubMajor(models.Model):
    university = models.ForeignKey('University', models.DO_NOTHING)
    level = models.ForeignKey('Level', models.DO_NOTHING)
    major = models.ForeignKey('Major', models.DO_NOTHING)
    submajor = models.ForeignKey('SubMajor', models.DO_NOTHING, blank=True, null=True)
    title = models.ForeignKey('SubMajorTitle', models.DO_NOTHING, blank=False, null=False)

    completion_time = models.TextField(blank=True, null=True, default=None)
    cost_per_year = models.TextField(blank=True, null=True, default=None)
    detail_link = models.TextField(blank=True, null=True, default=None)
    requirement_for_nepali = models.TextField(blank=True, null=True, default=None)

    start_date = models.ManyToManyField('Dates')
    scholarship_detail = models.ManyToManyField('UniversityCourseScholarship')
    entry_requirement = models.ManyToManyField('SubMajorEntryRequirement')

    detail = models.ManyToManyField('CourseItems')
    english_requirement = models.ManyToManyField('SubMajorEnglishRequirement')
    admission_process = models.ManyToManyField('UniversityCourseScholoarshipItem')
    other_expenses = models.ManyToManyField('SubMajorOtherExpenses')

    @staticmethod
    def get_chain_for_university(university: University):
        sub_majors = UniversitySubMajor.objects.filter(university=university)
        levels = {}
        for x in sub_majors:
            # verify that level exists
            if x.level.name not in levels:
                levels[x.level.name] = {}
            level = levels[x.level.name]

            if x.major.name not in level:
                level[x.major.name] = {}
            level[x.major.name][x.title.name] = x.title.pk
        return levels, len(sub_majors)

    def get_detail_info(self):
        data = {
            "id": self.pk,
            'title': self.title,
            'major_id': self.major.pk,
            'major': self.major.name if self.major else "Unknown",
            'level_id': self.level.pk,
            'level': self.level if self.level.name else 'Unknown',
            'duration': self.completion_time if self.completion_time else 'Unknown',
            "scholarship_detail": "Available" if self.scholarship_detail else "Unavailable",
            "start_date": [x for x in self.start_date] if self.start_date else "Unknown",
            "tution_fees": self.cost_per_year if self.cost_per_year else "Unknown"
        }
        # entry_requirement done
        if self.entry_requirement:
            requirements = []
            for x in self.entry_requirement:
                requirements.append(x.content)
            data['requirements'] = requirements
        # scholarship_detail done
        if self.scholarship_detail:
            data['scholarship_detail'] = [
                {
                    'title': x.title.title,
                    'description': x.content
                }
                for x in self.scholarship_detail
            ]
        if self.detail:
            data['detail'] = [{'title': x.topic.title, 'description': [y.content for y in x.description]} for x in
                              self.detaildetail]
        return data

    def get_brief_info(self):

        return {
            "id": self.pk,
            'title': self.title,
            'level': self.level if self.level else 'Unknown',
            'duration': self.completion_time if self.completion_time else 'Unknown',
            "scholarship_detail": "Available" if self.scholarship_detail else "Unavailable",
            "start_data": self.start_date if self.start_date else "Unknown",
            "tution_fees": self.cost_per_year if self.cost_per_year else "Unknown"
        }


class RequirementType(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Requirement(models.Model):
    type = models.ForeignKey('RequirementType', models.DO_NOTHING)
    requirement_description = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True, default=None)


class SubMajor(models.Model):
    name = models.TextField(blank=True, null=True, default=None)


class SubMajorTitle(models.Model):
    name = models.TextField(blank=True, null=True, default=None)


class SubMajorStartDate(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    submajor = models.ForeignKey('SubMajor', blank=False, null=False)


class SubReqByUniversity(models.Model):
    r_id = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)


class Subjects(models.Model):
    sub_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    belongs_to = models.ForeignKey('SubMajor', models.DO_NOTHING, db_column='belongs_to')


class ProgramsOffered(models.Model):
    programoffered = models.CharField(max_length=20)  # Field name made lowercase.

    def __str__(self):
        return self.programoffered


class RankingType(models.Model):
    content = models.TextField(blank=True, null=True, default=None)


class Ranking(models.Model):
    university = models.ForeignKey('University', models.DO_NOTHING, blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)
    ranking_type = models.ForeignKey('RankingType', null=False, blank=False, default=None)
    type_reference_table = models.IntegerField(blank=True, null=True, default=None)


class SubHeader(models.Model):
    title = models.CharField(max_length=250)


class CourseItems(models.Model):
    topic = models.ForeignKey('UniversitySubMajorTopic')
    description = models.ManyToManyField('CourseItemDescription')


class CourseItemDescription(models.Model):
    content = models.TextField(blank=True, null=True, default=None)


class UniversitySubMajorTopic(models.Model):
    title = models.TextField(blank=True, null=True, default=None)


class SubMajorEnglishRequirement(models.Model):
    type = models.ForeignKey('RequirementType')
    score = models.TextField(default=None, null=True, blank=True)


class UniversityCourseScholarship(models.Model):
    description = models.ManyToManyField('UniversityCourseScholoarshipItem')
    web_url = models.TextField(blank=True, null=True, default=None)
    deadline = models.TextField(blank=True, null=True, default=None)
    amount = models.TextField(blank=True, null=True, default=None)


class UniversityCourseScholoarshipItem(models.Model):
    description = models.TextField()
    title = models.ForeignKey('UniversityCourseScholarshipItemTitle')


class UniversityCourseScholarshipItemTitle(models.Model):
    title = models.TextField(blank=True, null=True, default=None)


class SubMajorEntryRequirement(models.Model):
    content = models.TextField(blank=True, null=True, default=None)


class SubMajorOtherExpenses(models.Model):
    value = models.TextField(blank=True, null=True, default=None)
    title = title = models.ForeignKey('UniversityCourseScholarshipItemTitle')
