from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Rating
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
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

  
