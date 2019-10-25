from django.shortcuts import render
from .models import job

# Create your views here.
def home(request):
  
    return render(request, 'jobs/home.html')
     

def alldata(request):
    return render(request,'jobs/alldata.html' )