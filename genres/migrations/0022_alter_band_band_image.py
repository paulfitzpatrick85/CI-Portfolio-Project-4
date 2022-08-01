# Generated by Django 3.2.14 on 2022-07-31 07:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0021_alter_band_band_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='band_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]