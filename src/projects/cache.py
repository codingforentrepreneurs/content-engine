from django.core.cache import cache as django_cache
from .models import Project

def get_user_projects(username=None, limit=5, set_on_none=True):
    projects_qs = Project.objects.none()
    if username is not None:   
        cache_str = f'_user_project_cache_{username}'
        projects_qs = django_cache.get(cache_str)
        if projects_qs is None and set_on_none:
            projects_qs = Project.objects.filter(
                    owner__username__iexact=username
            ).order_by('-updated')[:limit]
            django_cache.set(cache_str, projects_qs)
    return projects_qs