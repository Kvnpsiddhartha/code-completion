from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

def upload_photo_path(instance,filename):
    return "/".join([str(instance.username),filename])

class User(AbstractUser):
    phone=models.CharField(max_length=10)
    photo=models.ImageField(upload_to=upload_photo_path)
    REQUIRED_FIELDS=['email','password','phone','photo']

class Folder(models.Model):
    parent_folder=models.ForeignKey('Folder',on_delete=models.CASCADE,related_name='sub_folders',null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='folders')
    name=models.CharField(max_length=255)
    modified_time=models.DateTimeField(auto_now=True)

class Program(models.Model):
    parent_folder=models.ForeignKey('Folder',on_delete=models.CASCADE,related_name='programs')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='programs')
    name=models.CharField(max_length=255)
    code=models.TextField()
    modified_time=models.DateTimeField(auto_now=True)
