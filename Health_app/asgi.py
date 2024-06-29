"""
ASGI config for Health_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from channels.auth import AuthMiddlewareStack # type: ignore
from channels.routing import ProtocolTypeRouter, URLRouter # type: ignore
from django.core.asgi import get_asgi_application
import chat.routing # type: ignore
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Health_app.settings")

application = get_asgi_application({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
