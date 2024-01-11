from django.conf import settings
from django.db import models
from django.urls import reverse
from cfehome.utils.generators import unique_slugify
from . import validators
User = settings.AUTH_USER_MODEL

class AnonymousProject():
    value = None
    is_activated = False

class Project(models.Model):
    owner = models.ForeignKey(User, null=True, related_name='owned_projects', on_delete=models.SET_NULL)
    title = models.CharField(max_length=120, null=True)
    description = models.TextField(blank=True, null=True)
    handle = models.SlugField(null=True, blank=True, unique=True, 
                              validators=[validators.validate_project_handle])
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, related_name='projects_added', on_delete=models.SET_NULL, null=True)
    added_by_username = models.CharField(max_length=120, null=True, blank=True)
    last_modified_by = models.ForeignKey(User, related_name='projects_changed', on_delete=models.SET_NULL, null=True)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"handle": self.handle})
    
    def get_delete_url(self):
        return reverse("projects:delete", kwargs={"handle": self.handle})
    
    def get_activate_url(self):
        return reverse("activate_project", kwargs={"handle": self.handle})
    
    def get_activation_url(self):
        return self.get_activate_url()

    @property
    def is_activated(self):
        return True

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_username= self.added_by.username
        if not self.handle:
            self.handle = unique_slugify(self, slug_field='handle', invalid_slug='create')
        super().save(*args, **kwargs)