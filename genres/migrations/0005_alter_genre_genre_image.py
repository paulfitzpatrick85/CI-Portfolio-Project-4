# Generated by Django 3.2.14 on 2022-08-26 18:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0004_alter_band_band_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_image',
            field=cloudinary.models.CloudinaryField(default='placeholder_ex9qjl.jpg', max_length=255, verbose_name='image'),
        ),
    ]
