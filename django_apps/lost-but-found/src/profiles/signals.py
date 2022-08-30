from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from . models import Profile


@receiver(post_save, sender=get_user_model(), dispatch_uid='create_profile')
def create_profile(sender, created, **kwargs):
    user = kwargs['instance']
    if created:
        Profile.objects.create(user=user)
