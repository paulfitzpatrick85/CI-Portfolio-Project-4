from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Weather post is draft or published/live
STATUS = ((0, 'Draft'), (1, 'Published'))   # -may not use


# genre model
class Genre(models.Model):
    genre_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='genre')  # if user is deleted, their posts are to
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    genre_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.genre_name


class Band(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='bands')
    # slug = models.SlugField(max_length=100, unique=True)  # taken from post/genre class
    band_name = models.CharField(max_length=80)
    band_email = models.EmailField()
    bio_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    Band_approved = models.BooleanField(default=False)   
    # status = models.IntegerField(choices=STATUS, default=0)
    # created_on = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['created_on']  # order post by create_on, from above, '-' means use descending order

    def __str__(self):
        return f"Band {self.bio_body} by {self.band_name}"  # add image when code working properly

