from django.db import models
from django.conf import settings
from django.utils import timezone

class Question(models.Model):
    question = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=255, null=False)
