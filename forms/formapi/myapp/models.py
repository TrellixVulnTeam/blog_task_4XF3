import email
from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    phone=models.PositiveIntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=30)