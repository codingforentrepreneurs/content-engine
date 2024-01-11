from django import forms

from .models import Item 


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title']

class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description']