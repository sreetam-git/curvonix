from django.shortcuts import render
from .models import About_us, Slider, Feedback
from service.models import Service
from .forms import EnquiryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def about_us(request):
    about_us = About_us.objects.get()
    return render(request, 'home/about.html',{
        "about_us": about_us
    })
    
def home(request):
    sliders = Slider.objects.all().order_by("-pk")
    about_us = About_us.objects.get()
    services = Service.objects.all().order_by('-pk')
    feedbacks = Feedback.objects.filter(status="1")
    return render(request, "home/index.html",{
        "sliders": sliders,
        "about_us": about_us,
        "services": services,
        "feedbacks": feedbacks
    })
    
    
def contact_us(request):
    about_us = About_us.objects.get()
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("contact-us"))
        else:
            print("Form is not valid")
            print(form.errors)
            
    return render(request, "home/contact.html",{
        "about_us": about_us
    })
    
