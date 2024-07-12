from django.contrib import admin
from .models import Job, Applicant

# Register your models here.

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','created_at')
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Job)
admin.site.register(Applicant, ApplicantAdmin)
