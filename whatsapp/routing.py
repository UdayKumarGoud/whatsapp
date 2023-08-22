# # myproject/routing.py
# from django.urls import path
# from chat.consumers import ChatConsumer

# websocket_urlpatterns = [
#     path('ws/chat/', ChatConsumer.as_asgi()),
# ]



from django.urls import path

from userchat.consumers import ChatConsumer, NotificationConsumer

websocket_urlpatterns = [
    path("chats/<conversation_name>/", ChatConsumer.as_asgi()),
    path("notifications/", NotificationConsumer.as_asgi()),
]
