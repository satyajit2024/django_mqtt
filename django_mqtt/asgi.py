import os 

from django.core.asgi import get_asgi_application 
from channels.routing import ProtocolTypeRouter , URLRouter
import mqtt_app.routing 
# from channels.auth import AuthMiddlewareStack 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_mqtt.settings") 

application = ProtocolTypeRouter({ 
"http": get_asgi_application(), 
"websocket": URLRouter( 
			mqtt_app.routing.websocket_urlpatterns 
		)
}) 
