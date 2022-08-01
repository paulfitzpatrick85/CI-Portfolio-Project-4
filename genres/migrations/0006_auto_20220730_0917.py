# Generated by Django 3.2.14 on 2022-07-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0005_delete_genre_lite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='Band_approved',
            new_name='band_approved',
        ),
        migrations.RenameField(
            model_name='band',
            old_name='bio_body',
            new_name='band_bio',
        ),
        migrations.AddField(
            model_name='band',
            name='upcoming_tour_dates',
            field=models.TextField(default='TBA'),
        ),
    ]