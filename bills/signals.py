from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import CustomUser as User
from apartments.models import *

from .models import Wallet


@receiver(post_save, sender=User)
def post_save_create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(occupant_id=instance.id)
