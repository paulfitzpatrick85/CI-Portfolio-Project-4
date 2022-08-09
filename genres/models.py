from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  

# from datetime import datetime
# from django.utils import timezone

# Weather post is draft or published/live
STATUS = ((0, 'Draft'), (1, 'Published'))   # -may not use


# genre models
class Genre(models.Model):
    genre_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='genre_section') 
    content = models.TextField()
    genre_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)  
    approved = models.BooleanField(default=False)  
    
    
    def __str__(self):
        return self.genre_name


class Band(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='bands')
    # slug = models.SlugField(default='genre', unique=True)  
    band_name = models.CharField(max_length=80)
    band_email = models.EmailField()
    band_bio = models.TextField()
    band_image = CloudinaryField('image', default='placeholder')
    next_gig = models.TextField(default='DD-MM-YYYY')
    concert_venue = models.CharField(max_length=30, default='TBA')
    status = models.IntegerField(choices=STATUS, default=0)   #change from 0
    band_approved = models.BooleanField(default=False)   #change from false

    
    def __str__(self):
        return self.band_name 