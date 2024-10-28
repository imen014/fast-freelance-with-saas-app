from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from fastfreelance import settings

from Blogger.views import create_blog_and_image, get_blogs_images, get_my_blogs_and_images, modify_blog_image, delete_blog_image



urlpatterns = [
     path('create_blog_and_image/', create_blog_and_image, name='create_blog_and_image'),
    path('get_blogs_images/', get_blogs_images, name='get_blogs_images'),
    path('get_my_blogs_and_images/', get_my_blogs_and_images, name='get_my_blogs_and_images'),
    path('modify_blog_image/<int:id>/modify', modify_blog_image, name='modify_blog_image'),
    path('delete_blog_image/<int:id>/delete', delete_blog_image, name='delete_blog_image'),



]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
