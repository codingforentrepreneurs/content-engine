from functools import wraps
from django.shortcuts import render

from . import cache as project_cache

def project_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # logic
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        if not request.project.is_activated and username is not None:
            projects_qs = project_cache.get_user_projects(username=username)
            return render(request, "projects/project-required.html", {
                "object_list": projects_qs,
            })
        return view_func(request, *args, **kwargs)
    return _wrapped_view
