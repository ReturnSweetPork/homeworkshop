from django import forms
from .models import Student

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
