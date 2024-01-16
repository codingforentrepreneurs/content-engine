from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from projects.models import Project, AnonymousProject

# from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required as login_required

from django.shortcuts import redirect, render, get_object_or_404

from . import forms

PROJECT_CAN_DELETE_ITEM_THRESHOLD = 2

def get_project_or_404(request, handle=None, skip_404=False):
    object_list = Project.objects.filter(handle=handle).has_access(request.user)
    if not object_list.exists() and not skip_404:
        raise Http404
    if not object_list.exists() and skip_404:
        return None
    return object_list.first() 

@login_required
def project_list_view(request):
    object_list = Project.objects.has_access(request.user)
    return render(request, "projects/list.html", {'object_list': object_list})

@login_required
def project_detail_update_view(request, handle=None):
    instance = get_project_or_404(request, handle=handle)
    items_qs = instance.item_set.all()
    form = forms.ProjectUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        project_obj = form.save(commit=False)
        project_obj.last_modified_by = request.user 
        project_obj.save()
        return redirect(project_obj.get_absolute_url())
    context = {
        "instance": instance,
        "items_qs": items_qs,
        "form": form,
    }
    return render(request, "projects/detail.html", context)

@login_required
def project_delete_view(request, handle=None):
    instance = get_project_or_404(request, handle=handle)
    items_qs = instance.item_set.all()
    items_count = items_qs.count()
    items_exists = items_qs.exists()
    if request.method == "POST":
        if items_exists and items_count >= PROJECT_CAN_DELETE_ITEM_THRESHOLD:
            messages.error(request, f"Cannot delete project with {PROJECT_CAN_DELETE_ITEM_THRESHOLD} or more active items")
            return redirect(instance.get_delete_url())
        instance.delete()
        return redirect("projects:list")
    return render(request, "projects/delete.html", {"instance": instance})


# @project_required
@login_required
def project_create_view(request):
    if not request.project.is_activated:
        return render(request, 'projects/activate.html', {})
    form = forms.ProjectCreateForm(request.POST or None)
    if form.is_valid():
        project_obj = form.save(commit=False)
        project_obj.owner = request.user
        project_obj.added_by = request.user 
        project_obj.save()
        return redirect(project_obj.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, 'projects/create.html', context)


def delete_project_from_session(request):
    try:
        del request.session['project_handle']
    except:
        pass

def activate_project_view(request, handle=None):
    # http://localhost:8000/activate/project/content-engine
    project_obj = get_project_or_404(request, handle=handle, skip_404=True)
    if project_obj is None:
        delete_project_from_session(request)
        messages.error(request, "Project could not activate. try again.")
        return redirect("/projects")
    request.session['project_handle'] = handle
    messages.success(request, "Project activated.")
    return redirect("/")


def deactivate_project_view(request, handle=None):
    delete_project_from_session(request)
    messages.error(request, "Project deactivated.")
    return redirect("/")