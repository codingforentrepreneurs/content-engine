from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from cfehome.utils.generators import unique_slugify
from . import validators
User = settings.AUTH_USER_MODEL

class AnonymousProject():
    value = None
    is_activated = False

class ProjectUser(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)
    # edit = models.BooleanField(default=True)

class ProjectQuerySet(models.QuerySet):
    def has_access(self, user=None):
        if user is None:
            return self.none()
        return self.filter(
            Q(owner=user) |
            Q(projectuser__user=user, 
              projectuser__active=True)
        )
    def has_access_by_username(self, username=None):
        # Added off video recordings
        # for the project cache
        if username is None:
            return self.none()
        return self.filter(
            Q(owner__username__iexact=username) |
            Q(projectuser__user__username__iexact=username, 
              projectuser__active=True)
        )
    
class ProjectManager(models.Manager):
    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def has_access(self, user=None):
        return self.get_queryset().has_access(user=user)

class Project(models.Model):
    owner = models.ForeignKey(User, null=True, related_name='owned_projects', on_delete=models.SET_NULL)
    users = models.ManyToManyField(User, blank=True, 
                                related_name='projects',
                                through=ProjectUser)
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

    objects = ProjectManager()

    def __str__(self):
        return self.handle
    
    def get_prefix(self, trailing_slash=True):
        """
        S3 Prefix
        """
        if trailing_slash:
            return f"projects/{self.id}/"
        return f"projects/{self.id}"

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