from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40, default='')
    roll = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=10, default='')
    grade = models.CharField(max_length=20, default='')
    subjects = models.CharField(max_length=100, default='')
    email = models.EmailField(blank=None, default='')
    message = models.TextField(default='')
    image = models.ImageField(upload_to='images', null=True, blank=True)
