from django.db import models
from django.conf import settings
from django.urls import reverse # django-hosts
from projects.models import Project

User = settings.AUTH_USER_MODEL

# user.items_added
# user.items_changed

class Item(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, related_name='items_added', on_delete=models.SET_NULL, null=True)
    added_by_username = models.CharField(max_length=120, null=True, blank=True)
    last_modified_by = models.ForeignKey(User, related_name='items_changed', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_username= self.added_by.username
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return f"/items/{self.id}/"
        return reverse("items:detail", kwargs={"id": self.id})