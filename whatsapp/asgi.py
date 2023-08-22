"""
ASGI config for whatsapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsapp.settings')

# application = get_asgi_application()


# Import websocket application here, so apps from django_application are loaded first
from . import routing  # noqa isort:skip
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa isort:skip
from userchat.middleware import TokenAuthMiddleware  # noqa isort:skip


# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)),
#     }
# )


# from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from . import routing

application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application() ,
        "websocket" : TokenAuthMiddleware(
            URLRouter(
                routing.websocket_urlpatterns
            )   
        )
    }
)
