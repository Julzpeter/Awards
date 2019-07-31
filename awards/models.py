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


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(user__icontains=search_term)
        return profiles


class Project(models.Model):
    owner = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="user_name")
    profile = models.ForeignKey(Profile, null=True)
    sitename = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    screenshot = models.ImageField(
        upload_to='photos/', default='photos/default.jpg')
    optional_screenshot = models.ImageField(
        upload_to='photos/', default='photos/default.jpg')
    link = models.CharField(max_length=50)
    technologies = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
