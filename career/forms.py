from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        # fields = ['full_name', 'email', 'mobile_number', 'resume', 'job_id']
        exclude = ['created_at','updated_at','job']
        labels = {
            "full_name": "Full Name",
            "email": "Email address",
            "mobile_number": "Phone Number",
            "resume": "Upload Your Resume"
        }
