# Generated by Django 5.1.4 on 2024-12-16 14:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhotelsite', '0004_alter_review_stars_alter_roomimage_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='country',
            field=models.ForeignKey(max_length=32, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_country', to='myhotelsite.country'),
        ),
    ]