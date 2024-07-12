from django.shortcuts import render
from django.urls import reverse
from .models import Job
from home.models import About_us
from .forms import ApplicantForm
from django.http import HttpResponseRedirect

# Create your views here.

def career_home(request):
    jobs = Job.objects.all().order_by("-pk")
    about_us = About_us.objects.get()
    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            # print("Form is valid")
            try:
                # print(request.POST['job_id'])
                job_details = Job.objects.get(pk=request.POST['job_id'])
                applicant = form.save(commit=False)
                applicant.job = job_details
                applicant.save()
                print("Applicant saved successfully")
                return HttpResponseRedirect(reverse("career"))
            except Job.DoesNotExist:
                # print("Job not found")
                form.add_error('job_id', 'Job not found')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ApplicantForm()

    return render(request, "career/careers.html", {
        "jobs": jobs,
        "form": form,
        "about_us": about_us
    })
    
    
