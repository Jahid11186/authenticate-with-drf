from django.db import models
from .strings import ROLE_CHOICE


class ManagementModel(models.Model):
    role = models.CharField(max_length=10, choices=ROLE_CHOICE)

    class Meta:
        abstract = True
