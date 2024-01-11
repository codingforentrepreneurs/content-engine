from .models import Project
from . import cache as project_cache

def user_projects_context(request):
    username = None
    projects_qs = Project.objects.none()
    if request.user.is_authenticated:
        username = request.user.username
        projects_qs = project_cache.get_user_projects(username=username)
    return {
        "project_list": projects_qs,
    }