from django.db import models

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from apps.users.models import Profile


class PaymentTransaction(models.Model):
    hire_transaction = models.OneToOneField('rents.HireTransaction', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


@receiver(post_save, sender=PaymentTransaction)
def payment_transaction_created(sender, instance, created, **kwargs):
    profile = Profile.objects.get(user=instance.hire_transaction.user)
    profile.balance = profile.balance-instance.price
    profile.save()
