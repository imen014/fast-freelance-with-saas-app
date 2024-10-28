from django.db import models

class VideoLoader(models.Model):
    video = models.FileField()
    titre = models.CharField(max_length=255)
    creator = models.CharField(max_length=50)
