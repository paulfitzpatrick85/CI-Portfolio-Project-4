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
    # slug = models.SlugField(max_length=100, unique=True)  
    band_name = models.CharField(max_length=80)
    band_email = models.EmailField()
    band_bio = models.TextField()
    # band_image = models.ImageField(upload_to='images', default='/images/default-genre-photo.jpg')
    
    band_approved = models.BooleanField(default=False)
    upcoming_tour_dates = models.TextField(default='TBA')
    status = models.IntegerField(choices=STATUS, default=0)
    # variations i have tried
    # band_image = models.ImageField(upload_to='images')
    band_image = CloudinaryField('image', default='placeholder')
    # band_image = models.ImageField(upload_to='https://cloudinary.com/console/c-c24d22f1b451dca182670b2cf976ec/media_library/folders/c12896f112895c0f6e31ef0d8155d6ec0a', default='/images/default-genre-photo.jpg')
    # band_image = models.ImageField(upload_to='images', default='/images/default-genre-photo.jpg')
    
    def __str__(self):
        return f"Band {self.band_image}, {self.band_bio} by {self.band_name}" 