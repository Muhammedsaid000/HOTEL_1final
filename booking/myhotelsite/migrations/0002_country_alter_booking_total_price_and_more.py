# Generated by Django 5.1.4 on 2024-12-11 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhotelsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='country',
            field=models.ForeignKey(max_length=32, on_delete=django.db.models.deletion.CASCADE, to='myhotelsite.country'),
        ),
    ]