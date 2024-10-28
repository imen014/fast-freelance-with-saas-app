from django.db import models

class AudioStoreSaver(models.Model):
    audio = models.FileField()
    text = models.CharField(max_length=255)
    image = models.ImageField()