# Generated by Django 5.1.4 on 2024-12-18 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhotelsite', '0007_room_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='user',
            new_name='user_name',
        ),
    ]
