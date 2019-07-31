from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    bio = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        upload_to='photos/', default='photos/default.jpg')
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=12)
