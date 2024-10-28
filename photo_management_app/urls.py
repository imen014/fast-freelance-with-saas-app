"""
URL configuration for photo_management_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from photo_management_app.views import upload_photo, home, modifier_photo, delete_photo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_photo/', upload_photo, name='upload-photo'),
    path('', home, name='home_page'),
    path('modifier_photo/<int:id>/modify', modifier_photo, name='modifier-photo'),
    path('delete_photo/<int:id>/delete', delete_photo, name='delete-photo'),
]



if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
