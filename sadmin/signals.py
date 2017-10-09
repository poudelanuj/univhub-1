from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
import datetime


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    print("hello")
