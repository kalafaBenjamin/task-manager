from django.conf import settings
from django.db import models

from common.models import TimeStampedModel


class Project(TimeStampedModel):

    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="projects")

    def __str__(self):
        return self.name