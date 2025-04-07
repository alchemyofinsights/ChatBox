from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('', views.home, name='home'),         # GET /chat/ => home view
    path('home/', views.home, name='home'),    # Optional: /chat/home/
    path('join/', views.join_room, name='join_room'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('create/', views.create_room, name='create_room'),

]
