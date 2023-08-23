from django.db import models


class ModelTimeTracking(models.Model):
    """
    Abstract model to track date and time when records were created and updated.
    """

    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        abstract = True
