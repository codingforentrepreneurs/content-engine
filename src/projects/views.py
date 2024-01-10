from django.shortcuts import render, redirect
from django.contrib import messages
from projects.models import Project

def delete_project_from_session(request):
    try:
        del request.session['project_handle']
    except:
        pass

def activate_project_view(request, handle=None):
    # http://localhost:8000/activate/project/content-engine
    try:
        project_obj = Project.objects.get(owner=request.user, handle=handle)
    except:
        project_obj = None
        print("not here")
    if project_obj is None:
        delete_project_from_session(request)
        messages.error(request, "Project could not activate. try again.")
        return redirect("/projects")
    request.session['project_handle'] = handle
    messages.error(request, "Project activated.")
    return redirect("/")


def deactivate_project_view(request, handle=None):
    delete_project_from_session(request)
    messages.error(request, "Project deactivated.")
    return redirect("/")