from django import forms
from todoapp.models import Task

class TodoForm(forms.ModelForm):
    class Meta:
        # model to be edited
        model=Task
        # fields to edit
        fields=['name','priority','date']
