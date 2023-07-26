from django.shortcuts import render ,redirect
from .models import Number
 # Create your views here.


def index(request):
    

     nums = Number.objects.all()
     return render(request,"index.html" ,{"nums":nums})
 

 
