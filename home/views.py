from django.shortcuts import render
from .models import About_us

# Create your views here.

def about_us(request):
    about_us = About_us.objects.get()
    return render(request, 'home/about.html',{
        "about_us": about_us
    })
