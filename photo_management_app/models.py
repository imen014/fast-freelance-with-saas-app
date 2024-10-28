from django.db import models


class PhotoModel(models.Model):
    image = models.ImageField(verbose_name='images')
    uploader = models.CharField(max_length=255, default='sahar')
    caption = models.CharField(max_length=255, verbose_name='légende')
    date_creation = models.DateTimeField(auto_now_add=True)
