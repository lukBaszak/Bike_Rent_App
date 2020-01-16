from datetime import datetime

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import random

def create_unique_qr_code_identifier():
    while True:
        code = random.randint(1000000, 100000000)
        if not Profile.objects.filter(qr_identifier=code).exists():
            return code

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(default=datetime.now())
    phone_number = PhoneNumberField(null=True)
    qr_identifier = models.BigIntegerField(unique=True,default=create_unique_qr_code_identifier)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
