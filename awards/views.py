from django.shortcuts import render, redirect

# Create your views here.
from awards.forms import NewProjectForm
from awards.models import Profile, Project


def welcome(request):
    title = 'welcome to ip awards'
    profile = Profile.objects.all()
    return render(request, 'index.html', locals())

def new_project(request):
    my_user = request.user

    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = my_user
            profile.save()
            return redirect('welcome')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


def projects(request):

    projects = Project.objects.all()
    return render(request, 'index.html', locals())
