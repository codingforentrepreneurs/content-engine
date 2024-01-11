from django.core.cache import cache
from .models import Project

def user_projects_context(request):
    projects_qs = Project.objects.none()
    if request.user.is_authenticated:   
        cache_str = f'_user_project_cache_{request.user.username}'
        projects_qs = cache.get(cache_str)
        if projects_qs is None:
            projects_qs = Project.objects.filter(owner=request.user)
            cache.set(cache_str, projects_qs)
    return {
        "project_list": projects_qs,
    }