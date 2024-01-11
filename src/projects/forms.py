from django import forms

from .models import Project 


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'handle']

    # def clean_handle(self):
    #     handle = self.cleaned_data.get('handle')
    #     if handle == "create":
    #         raise forms.ValidationError(f"Create cannot be a hanlde")
    #     return handle

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'handle']
    
    # def clean_handle(self):
    #     handle = self.cleaned_data.get('handle')
    #     if handle == "create":
    #         raise forms.ValidationError(f"Create cannot be a hanlde")
    #     return handle