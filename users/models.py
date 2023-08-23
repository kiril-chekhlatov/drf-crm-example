from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import ModelTimeTracking
from users.helpers import FilePaths, Roles


class AdminUser(AbstractUser, ModelTimeTracking):
    appointment = models.TextField(verbose_name="Appointment", blank=True, null=True)
    role = models.PositiveSmallIntegerField(
        verbose_name="Role", choices=Roles.ROLE_CHOICES, blank=True, null=True
    )
    middle_name = models.CharField(
        verbose_name="Middle Name", max_length=30, blank=True, null=True
    )
    photo = models.FileField(
        verbose_name="Photo avatar",
        upload_to=FilePaths.get_photo_path,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Admin User"
        verbose_name_plural = "Admin Users"
