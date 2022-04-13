from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='myapp/media/images')
