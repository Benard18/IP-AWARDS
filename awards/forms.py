from django import forms

from awards.models import Project


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'categories']