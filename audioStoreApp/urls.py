from django.urls import path
from fastfreelance import settings
from django.conf.urls.static import static
from audioStoreApp.views import create_memory, get_memories, modify_memory, delete_memory, delete_memories
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioStoreSaverViewSet

router = DefaultRouter()
router.register(r'audios', AudioStoreSaverViewSet)

urlpatterns = [
    path('create_memory/',create_memory,name="create_memory"),
    path('get_memories/', get_memories, name="get_memories"),
    path('modify_memory/<int:id>/update', modify_memory, name="modify_memory"),
    path('delete_memory/<int:id>/',delete_memory,name="delete_memory"),
    path('delete_memories/', delete_memories, name="delete_memories"),
    path('api/', include(router.urls)),

]





urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)