from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "About us"
    
    def __str__(self):
        return self.main_content
    
