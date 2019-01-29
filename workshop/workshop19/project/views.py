from django.shortcuts import render, redirect
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.order_by("birthday").all()
    return render(request, "project/index.html", {"projects":projects})
    
    
def new(request):
    return render(request, "project/new.html")
    
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    project = Project(name=name, email=email, birthday=birthday, age=age)
    
    project.save()
    return redirect("/projects")
    
def read(request, id):
    project = Project.objects.get(pk=id)
    
    return render(request, "project/read.html", {'project':project})
    
def delete(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    
    
    return redirect("/projects")
    
def edit(request, id):
    project = Project.objects.get(pk=id)
    return render(request, "project/edit.html", {"project":project})

def update(request, id):
    project = Project.objects.get(pk=id)
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    project.name = name
    project.email = email
    project.birthday = birthday
    project.age = age
    
    project.save()
    
    return redirect(f"/projects/{id}/")
    