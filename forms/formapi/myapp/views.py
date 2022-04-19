from django.shortcuts import render
from django.views.generic.edit import FormView,CreateView
from .forms import *

# Create your views here.
class StudentForm(CreateView):
    model=Student
    fields=['name','phone','email','password']
    template_name='myapp/form.html'
    success_url='/'