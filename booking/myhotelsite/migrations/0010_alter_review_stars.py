# Generated by Django 5.1.4 on 2024-12-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhotelsite', '0009_rename_user_name_room_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='Рейтинг'),
        ),
    ]
