from django.shortcuts import render
from .models import Service
from home.models import About_us

# Create your views here.

def servicesList(request):
    about_us = About_us.objects.get()
    services = Service.objects.all().order_by("-pk")
    for service in services:
        print(service.image)
        if service.id % 2 == 0:
            service.is_even = True
        else:
            service.is_even = False
    return render(request, "service/services.html", {
        "services": services,
        "about_us": about_us
    })
