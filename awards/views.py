from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Rating
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import SubmitProjectForm, ProjectRatingForm, UpdateProfileForm
from django.db.models import Avg
# Create your views here.


@login_required(login_url='/accounts/login')
def home(request):
    users = User.objects.all()
    current = request.user
    projects = Project.objects.all()

    return render(request, 'index.html', {'users': users, 'user': current, 'projects': projects})

    # view function for users profile page


@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    user = User.objects.get(id=id)
    projects = Project.objects.filter(owner_id=id)
    if current_user.id == user.id:
        projects = Project.objects.filter(owner_id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)
    else:
        try:

            profile = Profile.objects.get(user_id=id)
        except ObjectDoesNotExist:

            return redirect(no_profile, id)

    return render(request, 'profile/profile.html', {'user': user, 'profile': profile, 'current_user': current_user, "projects": projects})

    # view function for updating profile page


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = id
            profile.save()
            return redirect(home)
    else:
        form = UpdateProfileForm()
    return render(request, 'profile/update_profile.html', {'user': user, 'form': form})

    # view function for a single_project
    def single_project(request, c_id):
        current_user = request.user
        current_project = Project.objects.get(id=c_id)
        ratings = Rating.objects.filter(project_id=c_id)
        usability = Rating.objects.filter(
        project_id=c_id).aggregate(Avg('usability_rating'))
        content = Rating.objects.filter(
        project_id=c_id).aggregate(Avg('content_rating'))
        design = Rating.objects.filter(
        project_id=c_id).aggregate(Avg('design_rating'))
        return render(request, 'project.html', {"project": current_project, "user": current_user, 'ratings': ratings, "design": design, "content": content, "usability": usability})


    

    
