# Generated by Django 3.2.14 on 2022-07-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0008_alter_band_band_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='band_image',
            field=models.ImageField(default='/images/default-genre-photo.jpg', upload_to='images'),
        ),
    ]
