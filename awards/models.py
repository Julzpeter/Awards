from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    # bio = models.CharField(max_length=200)
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
    link = models.CharField(max_length=200)
    technologies = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sitename

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        got_projects = Project.objects.filter(name__icontains=search_term)
        return got_projects


class Rating(models.Model):
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    usability_rating = models.IntegerField(
        default=0, choices=RATINGS, null=True)
    design_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    content_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.review

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    
