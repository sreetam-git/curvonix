from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class About_us(models.Model):
    main_content = RichTextUploadingField()
    main_image = models.ImageField(upload_to="about", help_text="Image size : 1500px X 1000px")
    sub_content = models.TextField()
    sub_image = models.ImageField(upload_to="about", help_text="Image size : 1500px X 1000px")
    home_content = models.TextField()
    image_one = models.ImageField(upload_to="about")
    image_two = models.ImageField(upload_to="about")
    image_three = models.ImageField(upload_to="about")
    image_four = models.ImageField(upload_to="about")
    what_we_do_content = models.TextField()
    contact_number = models.CharField(max_length=10, null=True)
    support_number = models.CharField(max_length=10, null=True)
    contact_email = models.EmailField(null=True)
    support_email = models.EmailField(null=True)
    office_address = models.TextField(null=True)
    logo = models.ImageField(upload_to="about", null=True)
    about_site = models.TextField(null=True)
    map_url = models.TextField(null=True)
    facebook_url = models.CharField(max_length=255,null=True)
    x_url = models.CharField(max_length=255, null=True)
    instagram_url = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "About us"
    
    def __str__(self):
        return self.main_content
    
    
class Slider(models.Model):
    class StatusTypes(models.TextChoices):
        ACTIVE = "1", _("Active")
        INACTIVE = "0", _("Inactive")
        
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="sliders")
    status = models.CharField(max_length=1, choices=StatusTypes, default=StatusTypes.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    

class Feedback(models.Model):
    class StatusTypes(models.TextChoices):
        ACTIVE = "1", _("Active")
        INACTIVE = "0", _("Inactive")
        
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to="feedback")
    designation = models.CharField(max_length=50)
    comment = models.TextField()
    status = models.CharField(max_length=1, choices=StatusTypes, default=StatusTypes.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name