import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ww2.settings')

import django
from django.core.asgi import get_asgi_application

django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from wsocket.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})