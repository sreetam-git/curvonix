from django.shortcuts import render
from .models import Service

# Create your views here.

def servicesList(request):
    services = Service.objects.all().order_by("-pk")
    for service in services:
        print(service.image)
        if service.id % 2 == 0:
            service.is_even = True
        else:
            service.is_even = False
    return render(request, "service/services.html", {
        "services": services
    })
