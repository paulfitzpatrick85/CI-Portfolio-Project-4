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


class Genre_lite(models.Model):
    genre_lite_name = models.CharField(max_length=200, unique=True)
    slug_lite = models.SlugField(max_length=200, unique=True)
    author_lite = models.ForeignKey(User, on_delete=models.CASCADE, related_name='genre_lite_section')  
    content_lite = models.TextField()
    genre_lite_image = CloudinaryField('image', default='placeholder')
    excerpt_lite = models.TextField(blank=True)
    status_lite = models.IntegerField(choices=STATUS, default=0)    
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.genre_lite_name


class Band(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='bands')
    # slug = models.SlugField(max_length=100, unique=True)  # taken from post/genre class
    band_name = models.CharField(max_length=80)
    band_email = models.EmailField()
    bio_body = models.TextField()
    band_image = CloudinaryField('image', default='placeholder')
    #created_on = models.DateTimeField(auto_now_add=True) 
    Band_approved = models.BooleanField(default=False)   
    # status = models.IntegerField(choices=STATUS, default=0)
    # created_on = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(upload_to='images')

    # class Meta:
    #     ordering = ['created_on']  # order post by create_on, from above, '-' means use descending order

    def __str__(self):
        return f"Band {self.bio_body} by {self.band_name}"  # add image when code working properly