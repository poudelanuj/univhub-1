import json
from university.models import *
from university.models import University as UniversityModel
from django.db import transaction
from itertools import chain


class University():
    saves = []
    title = {}
    sub_major = {}
    major = {}
    level = {}

    # initialize with a functioncall
    def __init__(self, file_name, pk=None):
        self.file = file_name
        self.university = json.load(open(file_name))
        if (not self.university['name']) or \
                (not self.university['location']):
            raise LookupError("Incomplete Data")

        self.db_university = UniversityModel.objects.get_or_create(
            name=self.university['name'],
            defaults={
                "logo_url": self.university['university_logo'],
                "main_line": self.university['motto'],
                "web_url": self.university['university_url']
            }
        )[0]
        self.uni_sub_major = {}

    # @University
    def insert_location(self):
        add = self.university['location']
        self.address = UniversityAddress.objects.get_or_create(
            university=self.db_university,
            country=add['country'],
            state=add['state'],
            city=add['city'],
            street=add['street'],
            postal_code=add['postal code'],
            is_main=True
        )[0]

    # @University
    def insert_highlight(self):
        for x in self.university['highlights']:
            hilit = HighlightText(content=x)
            hilit.save()
            map = HighlightMap(highlight=hilit, university=self.db_university)
            map.save()

    # @University
    def insert_world_ranking(self):
        ranking = RankingType.objects.get_or_create(content="World")[0]
        if self.university['world_ranking']:
            r = Ranking(university=self.db_university,
                        ranking=self.university['world_ranking'],
                        ranking_type=ranking,
                        )
            r.save()

    # @University
    def insert_detail_description(self):
        for content in self.university["detailed_desc"]:
            h = Header(content=content['topic'])
            h.save()
            uc = UniversityContent(university=self.db_university, header=h, description=content['description'])
            uc.save()

    # @Course --> same for hotcourse and shiksha
    @staticmethod
    def construct_sub_major_missing(courses_hot_course, courses_shiksha):

        titles_shiksha = set([x['title'] for x in courses_shiksha
                              if x['title'] is not None])
        titles_hot_course = set([x['title'] for x in courses_shiksha
                                 if x['title'] is not None])

        hot_course = []
        shiksha = []
        common_course = {}
        titles = []
        for x in courses_hot_course:
            if x['title'] is not None:
                if x['title'] in titles_shiksha:
                    common_course[x['title']].append(x)
                else:
                    titles.append(x['title'])
                    hot_course.append(x)

        for x in courses_shiksha:
            if x['title'] is not None:
                if x['title'] in titles_hot_course:
                    common_course[x['title']] = [x]
                else:
                    titles.append(x['title'])
                    shiksha.append(x)

        sub_majors = set([x['submajor'] for x in courses_shiksha
                          if x['submajor'] is not None
                          and x['submajor'] not in University.sub_major])
        sub_majors.update([x['submajor'] for x in courses_hot_course
                           if x['submajor'] is not None
                           and x['submajor'] not in University.sub_major]
                          )

        majors = [x['major'] for x in courses_shiksha
                  if x['major'] is not None
                  and x['major'] not in University.major]
        majors.update([x['major'] for x in courses_hot_course
                       if x['major'] is not None
                       and x['major'] not in University.major])

        levels = [x['type'] for x in courses_shiksha
                  if x['type'] is not None
                  and x['type'] not in University.level]
        levels.update([x['type'] for x in courses_hot_course
                       if x['type'] is not None
                       and x['type'] not in University.level])
        for x in majors:
            major = Major(name=x)
            major.save()
            University.major[x] = major

        for x in sub_majors:
            submajor = SubMajor(name=x)
            submajor.save()
            University.sub_major[x] = submajor

        for x in titles:
            title = SubMajorTitle(name=x)
            title.save()
            University.title[x] = title

        for x in levels:
            level = Level(name=x)
            level.save()
            University.level[x] = level
        return common_course, hot_course, shiksha

    def insert_admission_process_shiksha(self, course, uni_sub_major: UniversitySubMajor):
        if course['admission_process']:
            for x in course['admission_process']:
                scholarship = UniversityCourseScholoarshipItem(
                    title=UniversityCourseScholarshipItemTitle(title=x['topic']),
                    description=x['description']
                ).save()
                uni_sub_major.scholarship_detail.add(scholarship)

    # @hotcourse
    def insert_or_get_course_hot_course(self, course):
        # return if already inserted
        if course['title'].lower() in self.uni_sub_major:
            return self.uni_sub_major[course['title'].lower()]
        # first make the university_sub_major table

        uni_sub_major = UniversitySubMajor(
            university=self.db_university,
            title=University.title[course['title']],

            level=University.level[course['type']],
            major=University.major[course['major']],
            submajor=University.sub_major[course['submajor']],
            completion_time=course['full_time'],
            cost_per_year=course['cost_per_year'],
            detail_link=course['course_details_link']
        )
        uni_sub_major.save

        self.uni_sub_major[course['title']] = uni_sub_major
        self.uni_sub_major['title'] = course['title'].lower()
        return uni_sub_major

    @staticmethod
    def insert_course_expenses_shiksha(course, uni_sub_major):
        if course['other_expenses']:
            for x in course['other_expenses']:
                exp = SubMajorOtherExpenses(
                    title=UniversityCourseScholarshipItemTitle(title=x['component']),
                    value=x['amount']
                ).save()
                uni_sub_major.other_expenses.add(exp)

    # @hotcourse
    def insert_course_start_date_hot_course(self, course, uni_sub_major):
        if course['start_date']:
            for x in course['start_date']:
                date = Dates.objects.get_or_create(date=x)[0]
                uni_sub_major.start_date.add(date)

    # @hot_course
    def insert_course_detail_hot_course(self, course, uni_sub_major):
        if not course['course_details']:
            return
        if not course['course_details']['items']:
            return
        for section in course['course_details']['items']:
            # TODO get_or_create here.
            topic = UniversitySubMajorTopic.objects.get_or_create(title=section['topic'])[0]
            item = CourseItems(
                topic=topic
            )
            item.save()
            for desc in section['description']:
                desc = desc.replace('\u200b', ' ')
                description = CourseItemDescription(content=desc)
                description.save()
                item.description.add(description)
            item.save()
            uni_sub_major.detail.add(item)

    @staticmethod
    def insert_course_detail_shiksha(course, uni_sub_major):
        topic = UniversitySubMajorTopic.objects.get_or_create(title='About')[0]
        item = CourseItems(
            topic=topic
        )
        item.save()
        for desc in course['course_details']:
            desc = desc.replace('\u200b', ' ')
            description = CourseItemDescription(content=desc)
            description.save()
            item.description.add(description)
        item.save()
        uni_sub_major.detail.add(item)

    # @shiksha
    @staticmethod
    def insert_course_requirement_shiksha(course, uni_sub_major: UniversitySubMajor):
        for x in course['entry_requirements']:
            entry_requirement = SubMajorEntryRequirement(content=x)
            entry_requirement.save()
            uni_sub_major.entry_requirement.add(entry_requirement)

        for req in course['english_requirement']:
            # TODO : optimize this get_or_create
            _type = RequirementType.objects.get_or_create(name=req['type'])[0]
            db_req = SubMajorEnglishRequirement(
                type=_type,
                score=int(req['score'])
            )
            db_req.save()
            uni_sub_major.english_requirement.add(db_req)

    def insert_course_requirement_hot_course(self, course, uni_sub_major: UniversitySubMajor):
        uni_sub_major.requirement_for_nepali = course['entry_requirements'][0]['desc']

    # @shiksha
    @staticmethod
    def insert_course_scholarship(scholarship, uni_sub_major):
        for item in scholarship['items']:
            title = UniversityCourseScholarshipItemTitle.objects.get_or_create(item['topic'])[0]
            description = CourseItemDescription(title=title, content=item['description'].replace('\u200b', ' '))
            description.save()

        db_scholarship = UniversityCourseScholarship(
            description=description,
            web_url=scholarship['campus_scholarship_link'][0],
            deadline=scholarship['scholarship_deadline'],
            amount=scholarship['scholarship_amount']
        )
        db_scholarship.save()
        uni_sub_major.scholarship = db_scholarship

    @staticmethod
    def load_sub_major_hash():
        for _major in Major.objects.all():
            University.major[_major.name] = _major
        for _level in Level.objects.all():
            University.level[_level.name] = _level
        for _sub_major in SubMajor.objects.all():
            University.sub_major[_sub_major.name] = _sub_major
        for _title in SubMajorTitle.objects.all():
            University.title[_title.name] = _title

        # create unknown fields for all the major and submajor fields
        if 'Unknown' not in University.major:
            unknown = Major(name="Unknown")
            unknown.save()
            University.major[None] = unknown
        if 'Unknown' not in University.level:
            unknown = Level(name="Unknown")
            unknown.save()
            University.level[None] = unknown
        if 'Unknown' not in University.sub_major:
            unknown = SubMajor(name="Unknown")
            unknown.save()
            University.sub_major[None] = unknown
        if 'Unknown' not in University.title:
            unknown = SubMajorTitle(name="Unknown")
            unknown.save()
            University.title[None] = unknown

    def insert_requirements(self):
        # TODO: University requirement is not done.
        pass

    def insertion_sequence(self):
        sequence = [
            {
                "name": "Insert University Detail",
                "operation": University.insert_course_detail,
            },
            {
                "name": "Insert University Highlight",
                "operation": University.insert_highlight,
            },
            {
                "name": "Insert University Location",
                "operation": University.insert_location, },
            {
                "name": "Insert University Wrold ranking",
                "operation": University.insert_world_ranking
            }
        ]

        with transaction.atomic():
            # the sequence of  following function calls
            #  can be interchanged with no side effect.
            self.insert_location()
            self.insert_highlight()
            self.insert_world_ranking()
            self.insert_detail_description()

            # before doing anything load all the required courses
            # if it doesn't exist create it in database.
            hot = self.university['courses_hot_courses']
            shiksha = self.university['courses_shiksha']

            common, hot, skhiksha = self.construct_sub_major_missing(hot if hot else [], shiksha if shiksha else [])

            for course_hot, course_shiksha in common:
                with transaction.atomic():
                    print("common course :", course_hot['title'])
                    # creating a course table is first step
                    fk = self.insert_or_get_course_hot_course(course_hot)
                    # the sequence of following function calls
                    # can be interchanged with no side effects.
                    self.insert_course_start_date_hot_course(course_hot, fk)
                    self.insert_course_detail_hot_course(course_hot, fk)
                    self.insert_course_requirement_hot_course(course_hot, fk)

                    # no2 update from the shiksha one
                    # self.insert_course_detail_shiksha(course_shiksha, fk)
                    self.insert_course_requirement_shiksha(course_shiksha, fk)
                    self.insert_course_scholarship(course_shiksha['scolarship'], fk)
                    self.insert_admission_process_shiksha(course_shiksha)
                    self.insert_course_expenses_shiksha(course_shiksha)

            for course in hot:
                with transaction.atomic():
                    print("hot course only course :", course['title'])
                    # creating a course table is first step
                    fk = self.insert_or_get_course_hot_course(course)
                    # the sequence of following function calls
                    # can be interchanged with no side effects.
                    self.insert_course_start_date_hot_course(course, fk)
                    self.insert_course_detail_hot_course(course, fk)
                    self.insert_course_requirement_hot_course(course, fk)

            for course in shiksha:
                with transaction.atomic():
                    print("shiksha only course :", course['title'])
                    fk = self.insert_or_get_course_hot_course(course)
                    self.insert_course_detail_shiksha(course, fk)
                    self.insert_course_requirement_shiksha(course, fk)
                    self.insert_course_scholarship(course['scolarship'], fk)
                    self.insert_admission_process_shiksha(course)
                    self.insert_course_expenses_shiksha(course)

                    # now insert the courses from shiksha, but will be implemented in future

                    # let's ignore all the shiksha things.

                    # load the sub_major hashes initially


University.load_sub_major_hash()
