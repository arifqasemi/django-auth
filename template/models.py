from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=30, default='Unknown')
    first_name = models.CharField(max_length=30,  default='Unknown')
    last_name = models.CharField(max_length=30, default='Unknown')
    email = models.CharField('email', max_length=80, default='Unknown')
    password = models.CharField('password',max_length=50)

class UserProfiles(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='uploads', default='default.jpg')

    def __str__(self):
        return self.user.username