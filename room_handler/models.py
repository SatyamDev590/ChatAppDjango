from django.db import models


class Room(models.Model):
    room_name=models.CharField(max_length=100, unique=True)
    description=models.CharField(max_length=100, null=True, blank=True)
    port=models.IntegerField(help_text="contains port for websocket connection", null=True, blank=True)