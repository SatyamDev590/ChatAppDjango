# Generated by Django 4.2.11 on 2024-05-08 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_handler', '0003_room_port'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='room_name',
        ),
    ]
