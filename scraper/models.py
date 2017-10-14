from django.db import models
from django.utils import timezone
# Create your models here.
from university.models import University as UniversityModel


class ScrapingHistory(models.Model):
    university = models.ForeignKey(UniversityModel, null=False, blank=False, default=None)
    time = models.DateTimeField(auto_now=True)
    step = models.ForeignKey(ScrapingStep, null=True, blank=True)


class ScrapingStep(models.Model):
    depends_on = models.ForeignKey('ScrapingStep', null=True, blank=True, default=True)
    content = models.TextField()
