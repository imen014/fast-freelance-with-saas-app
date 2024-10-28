
from django.urls import path
from . import views

urlpatterns = [
    path('digital_service/create/', views.create_digital_service, name="create_digital_service"),
    path('digital_service/get/', views.get_all_digital_services, name="get_all_digital_services"),
    path('digital_service/own_services/', views.get_my_services, name="get_my_digital_services"),
    path('digital_service/<int:id>/delete', views.delete_digital_service, name="delete_digital_service"),
    path('digital_service/<int:id>/update', views.update_digital_service, name="update_digital_service"),
    path('digital_service/<int:id>/details', views.get_service_details, name="get_service_details"),
    path('get_my_balance', views.get_my_balance, name="get_my_balance"),
    path('get_my_buyed_services', views.get_my_buyed_services, name="get_my_buyed_services"),
    path('get_my_selled_services', views.get_my_selled_services, name="get_my_selled_services"),
    path('get_notifications', views.get_notifications, name="get_notifications"),
    path('sended_offres', views.sended_offres, name="sended_offres"),
    path('received_offres', views.received_offres, name="received_offres"),
    #path('get_user_services/<int:id>/', views.get_user_services , name="get_user_services"),




]
