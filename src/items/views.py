from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ItemForm
from .models import Item

# @project_required
@login_required
def item_create_view(request):
    if not request.project.is_activated:
        return render(request, 'projects/activate.html', {})
    form = ItemForm(request.POST or None)
    if form.is_valid():
        item_obj = form.save(commit=False)
        item_obj.project = request.project
        item_obj.added_by = request.user 
        item_obj.save()
        form = ItemForm()
    context = {
        "form": form
    }
    return render(request, 'items/create.html', context)