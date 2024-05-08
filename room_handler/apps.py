from django.apps import AppConfig


class RoomHandlerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'room_handler'

    def ready(self):
            import room_handler.signals