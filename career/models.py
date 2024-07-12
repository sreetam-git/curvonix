from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Job(models.Model):
    class StatusTypes(models.TextChoices):
        ACTIVE = "1", _("Active")
        INACTIVE = "0", _("Inactive")
        
    job_title = models.CharField(max_length=150)
    job_description = models.TextField()
    posted_on = models.DateField()
    location = models.CharField(max_length=255)
    experience = models.CharField(max_length=15)
    status = models.CharField(max_length=1, choices=StatusTypes, default=StatusTypes.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.job_title
    
    
class Applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applicants")
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10)
    resume = models.FileField(upload_to="career")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
