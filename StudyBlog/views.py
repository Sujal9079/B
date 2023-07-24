from django.shortcuts import render 
from .models import Number
 # Create your views here.


def index(request):
    

     nums = Number.objects.all()
     return render(request,"index.html" ,{"nums":nums})
 
     maps = Map.objects.all()
     return render(request,"index.html",{"maps":maps})
 
