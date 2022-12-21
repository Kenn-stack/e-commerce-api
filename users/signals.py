from django.dispatch import receiver
from django.db.models.signals import post_save

from .User import User

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()