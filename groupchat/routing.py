# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from . import consumers
# from django.core.asgi import get_asgi_application
# from userchat.middleware import TokenAuthMiddleware  # noqa isort:skip


# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": TokenAuthMiddleware(URLRouter([
#         path("ws/groupchat/<str:group_id>/", consumers.ChatConsumer.as_asgi()),
#     ]),
#     )
# })

# your_project/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from groupchat import consumers
from .middleware import TokenAuthMiddleware
from django.core.asgi import get_asgi_application
application = ProtocolTypeRouter({
    
    "websocket": TokenAuthMiddleware(
        URLRouter([
            path("ws/groupchat/<str:group_id>/", consumers.ChatConsumer.as_asgi()),
        ]),
    ),
    "http" : get_asgi_application(),
})


# routing.py
# from django.urls import re_path


# websocket_urlpatterns = [
#     re_path(r'ws/group/(?P<group_name>\w+)/$', consumers.GroupChatConsumer.as_asgi()),
# ]
