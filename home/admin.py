from django.contrib import admin
from .models import About_us

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('main_content', 'created_at', 'updated_at',)
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(About_us, AboutAdmin)