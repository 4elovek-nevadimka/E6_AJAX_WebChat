from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=User)
def notify_post_created(sender, instance, created, **kwargs):
    if created:
        # если создали новую учетку, то создать UserProfile
        UserProfile.objects.create(user=instance)
