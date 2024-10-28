from django.contrib import admin
from django.urls import path, include

from account_creation_app.views import create_account, show_account, get_accounts, see_informations, modify_profile, delete_account, login_user, home, logout_user

from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('audioStoreApp.urls')),
    path('', include('Blogger.urls')),
    path('', include('chat_app.urls')),
    path('', include('digiat_services_app.urls')),
    path('', include('photo_management_app.urls')),
    path('', include('videoStoreApp.urls')),


    path('admin/', admin.site.urls),
    path('create_account/', create_account, name='create_account'),
    path('show_account/<int:id>/showit', show_account, name='show_account'),
    path('get_accounts/', get_accounts, name='get_accounts'),
    path('see_informations/<int:id>/details', see_informations, name='see_informations'),
    path('modify_profile/<int:id>/modify', modify_profile, name='modify_profile'),
    path('delete_account/<int:id>/delete', delete_account, name='delete_account'),
    path('login_user/', login_user, name='login_user'),
    path('home/', home, name='home'),
    path('logout_user/', logout_user, name='logout_user'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
