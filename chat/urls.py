# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatListView.as_view(), name='chat_list'),
    path('<str:recipient_username>/', views.chat, name='chat'),
    # Add other views if necessary
]
