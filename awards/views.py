from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Rating
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    users = User.objects.all()
    current = request.user
    projects = Project.objects.all()

    return render(request, 'index.html', {'users': users, 'user': current, 'projects': projects})



