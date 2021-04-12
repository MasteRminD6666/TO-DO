from django import forms
from .models import Tasks

class aply_task(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['TO_DO']

class update_form(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['TO_DO', 'complete']