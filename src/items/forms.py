from django import forms

from .models import Item 


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description']

    def clean_title(self):
        raise forms.ValidationError("there was somthing wrong")

    def clean_description(self):
        raise forms.ValidationError("there was somthing wrong")