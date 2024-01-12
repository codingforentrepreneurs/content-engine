from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse 
from projects import cache as projects_cache
from django.http import HttpResponse
from django_htmx.http import trigger_client_event
from projects.decorators import project_required

from . import forms
from .models import Item

@project_required
@login_required
def item_list_view(request):
    object_list = Item.objects.filter(project=request.project)
    template_name = "items/list.html"
    if request.htmx:
        template_name = "items/snippets/table.html"
    return render(request, template_name, {'object_list': object_list})

@project_required
@login_required
def item_detail_update_view(request, id=None):
    instance = get_object_or_404(Item, id=id, project=request.project)
    form = forms.ItemUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        item_obj = form.save(commit=False)
        item_obj.last_modified_by = request.user 
        item_obj.save()
        return redirect(item_obj.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "items/detail.html", context)

@project_required
@login_required
def item_delete_view(request, id=None):
    instance = get_object_or_404(Item, id=id, project=request.project)
    if request.method == "POST":
        instance.delete()
        return redirect("items:list")
    return render(request, "items/delete.html", {"instance": instance})


@project_required
@login_required
def item_create_view(request):
    template_name = 'items/create.html'
    if request.htmx:
        template_name = 'items/snippets/form.html'
    form = forms.ItemCreateForm(request.POST or None)
    if form.is_valid():
        item_obj = form.save(commit=False)
        item_obj.project = request.project
        item_obj.added_by = request.user 
        item_obj.save()
        if request.htmx:
            custom_refresh_event = "refresh-list-view"
            response = HttpResponse("")
            return trigger_client_event(response,custom_refresh_event)
        return redirect(item_obj.get_absolute_url())
    action_create_url = reverse("items:create")
    context = {
        "form": form,
        "btn_label": "Create item",
        "action_url": action_create_url
    }
    return render(request, template_name, context)