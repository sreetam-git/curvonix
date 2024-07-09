from django.contrib import admin
from .models import Service

# Register your models here.

class serviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')
    list_filter = ('status',)
    
admin.site.register(Service, serviceAdmin)
