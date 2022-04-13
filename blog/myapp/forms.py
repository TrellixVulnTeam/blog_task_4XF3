from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Blog

class UserRegiistration(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
