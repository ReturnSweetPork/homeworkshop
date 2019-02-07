from django.shortcuts import render,redirect
from .models import App

# Create your views here.
def index(request):
    apps = App.objects.all()
    return render(request,"app/index.html",{"apps":apps})