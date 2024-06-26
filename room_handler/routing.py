from django.urls import path
from . import ws_api

websocket_urlpatterns=[
    path('ws/<str:room_name>/',ws_api.RoomChatConsumer.as_asgi()),
    path('ws/<str:sender>/<str:receiver>/',ws_api.PrivateChatConsumer.as_asgi())
]