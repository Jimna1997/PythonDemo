from django import forms
from movieapp.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        # model to be edited
        model=Movie
        # fields to edit
        fields=['name','desc','img','year']
