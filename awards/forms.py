from django import forms
from .models import Profile, Project, Rating
from django.contrib.auth.models import User


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class ProjectRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['project', 'pub_date', 'user']


class SubmitProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner', 'pub_date', 'profile']
