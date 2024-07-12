from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us', views.about_us, name="about-us"),
    path('contact-us', views.contact_us, name="contact-us"),
    path('submit-contact', views.contact_us, name="submit-contact")
]
