from django.db import models
from django.contrib.auth.models import AbstractUser



class Freelancer(AbstractUser):
    image = models.ImageField(verbose_name='images')
    image_title = models.CharField(max_length=100, default='profil photo', verbose_name='Profile picture')
    date_naissance = models.DateField(verbose_name='Date of birth', default='1993-10-25')
    lieu_residence = models.CharField(max_length=255,verbose_name='Place of residence')
    social_media=models.CharField(max_length=50, verbose_name='social media')
    description = models.CharField(max_length=255,verbose_name='Description')
    current_employment=models.CharField(max_length=255,verbose_name='current employment')
    academic_degrees=models.CharField(max_length=255, verbose_name='Academic degrees')
    professional_skills=models.CharField(max_length=255, verbose_name='professional skills')
    hobbies=models.CharField(max_length=255, verbose_name='hobbies')
