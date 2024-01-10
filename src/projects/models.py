from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Project(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120, null=True, blank=True)
    handle = models.SlugField(null=True, blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
