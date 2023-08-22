from django.urls import path
from . import views


app_name = 'group_app'

urlpatterns = [
    path('api/create_group/', views.create_group),
    path('api/user_status/<int:user_id>/', views.user_status),
    
    path('chat/<str:group_name>/', views.chat_room, name='chat_room'),
    
    path('', views.home, name='home'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
]