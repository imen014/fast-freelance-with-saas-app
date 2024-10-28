from django.db import models
from fastfreelance import settings




class ImageModel(models.Model):
    image=models.ImageField()
    #uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    caption = models.CharField(max_length=50, verbose_name="légende")



class BlogModel(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='blog title')
    blog_content=models.TextField(verbose_name='blog content')
    blog_image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    #blog_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

