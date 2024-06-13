from django.db import models
from django.conf import settings


class Task(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
