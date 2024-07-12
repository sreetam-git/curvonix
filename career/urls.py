from django.urls import path
from . import views

urlpatterns = [
    path('', views.career_home, name="career"),
    path('submit-application', views.career_home, name="submit_application")
]
