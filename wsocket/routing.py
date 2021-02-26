from django.urls import re_path

from wsocket.consumers import SocketConsumer

websocket_urlpatterns = [
    re_path(r'', SocketConsumer.as_asgi()),
]
