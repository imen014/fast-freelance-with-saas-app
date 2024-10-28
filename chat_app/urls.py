from django.urls import path
from fastfreelance import settings
from django.conf.urls.static import static
from chat_app import views
urlpatterns = [
    path('create_message/', views.create_message, name="create_message"),
    path('get_my_message/', views.get_my_message, name="get_my_message"),
    path('answer_message/', views.answer_message, name="answer_message"),
    path('answer_message_from_a_list/<int:id>/answer', views.answer_message_from_a_list, name="answer_choosed_message"),
    path('delete_all_my_messages/', views.delete_all_my_messages, name="delete_all_my_messages"),
    path('answer_an_answer_from_a_list/<int:id>/answer',views.answer_an_answer_from_a_list,name="answer_an_answer_from_a_list"),
] 




if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )