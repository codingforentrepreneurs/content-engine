from django.contrib import admin

# Register your models here.
from .models import Project, ProjectUser

class ProjectUserInline(admin.TabularInline):
    model = ProjectUser
    raw_id_fields = ['user']
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectUserInline]
    list_display = ['title', 'handle', 'owner']
    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)