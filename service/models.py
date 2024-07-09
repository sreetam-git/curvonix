from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="service_image", help_text="Image size : 256px X 256px")
    status = models.CharField(max_length=10 ,help_text="Please enter active or inactive.")
    
    def __str__(self):
        return self.title