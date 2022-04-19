
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Student
        fields='__all__'
        labels={'name':'Nirajan'}
        help_text={'email':'Enter your genuine email'}