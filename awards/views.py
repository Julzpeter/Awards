from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import Project, Profile, Rating
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import SubmitProjectForm, ProjectRatingForm, UpdateProfileForm
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg
# Create your views here.


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


def review_rating(request, id):
    current_user = request.user
    current_project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = current_project
            rating.user = current_user
            rating.save()
            return redirect('project', id)
    else:
        form = ProjectRatingForm()

    return render(request, 'rating/rating.html', {'form': form, "project": current_project, "user": current_user})


def new_project(request, id):
    current_user = request.user
    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)

    if request.method == 'POST':
        form = SubmitProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = current_user
            project.profile = Profile.objects.get(user_id=id)
            project.save()
        return redirect(home)

    else:
        form = SubmitProjectForm()

        return render(request, 'new_project.html', {'form': form, "user": current_user})


def search_results(request):
    if request.method == 'GET':

        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(sitename__icontains=query) | Q(
                content__icontains=query)

            searched_project = Project.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'searched.html', {"project": searched_project})

        else:
            return render(request, 'searched.html')

    else:
        return render(request, 'searched.html')

    return render(request, 'searched.html', {"project": searched_project})


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)


class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)
