from django.db import models
from sadmin.models import *
from university.models import *
# Create your models here.


class Process (models.Model):
    student = models.ForeignKey (Student, on_delete=models.CASCADE)
    country = models.ForeignKey (Country, on_delete=models.CASCADE)


class IntendedSubMajor (models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    submajor = models.ForeignKey(SubMajor, on_delete=models.CASCADE)


class IntendedUniversity(models.Model):
    process = models.Model(Process, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class ScoreProfile(Student):
    ieltsScore = models.IntegerField(blank=True, null=True)
    toeflScore = models.IntegerField(blank=True, null=True)
    satScore = models.IntegerField(blank=True, null=True)
    