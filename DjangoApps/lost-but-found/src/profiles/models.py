from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid
import os
from django_resized import ResizedImageField


def make_image_file_path(instance, filename):
    """Generate file path for new profile image"""
    ext = filename.split(".")[-1]
    filename = f"{instance.user.first_name}_{instance.user.last_name}-{uuid.uuid4()}.{ext}"
    return os.path.join("uploads/profile/", filename)


UserModel = get_user_model()


class Profile(models.Model):

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))
    date_of_birth = models.DateField(blank=True)
    country = models.CharField(max_length=256, blank=True)
    state = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)
    image = ResizedImageField(
        upload_to=make_image_file_path,
        null=True,
        size=[400, 400],
        quality=-1,
        scale=0.5,
        crop=["middle", "center"],
        blank=True,
    )

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"