from django.contrib import admin
from django.urls import path
from fastfreelance import settings
from django.conf.urls.static import static
from videoStoreApp.views import upload_video, get_videos, modify_video, delete_video, clear_box_videos
from django.urls import path
from .views import VideoLoaderListCreateView, VideoLoaderDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_video/', upload_video, name="upload_video"),
    path('get_videos/', get_videos, name="get_videos"),
    path('modify_video/<int:id>/modify', modify_video, name="modify_video"),
    path('delete_video/<int:id>/', delete_video, name="delete_video"),
    path('clear_box_videos/', clear_box_videos, name="clear_box_videos"),
     path('videos/', VideoLoaderListCreateView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoLoaderDetailView.as_view(), name='video-detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
