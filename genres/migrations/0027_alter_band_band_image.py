# Generated by Django 3.2.14 on 2022-07-31 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0026_alter_band_band_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='band_image',
            field=models.ImageField(default='placeholder', upload_to='images'),
        ),
    ]
