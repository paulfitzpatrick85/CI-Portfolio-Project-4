from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Weather post is draft or published/live
STATUS = ((0, 'Draft'), (1, 'Published'))


# genre models
class Genre(models.Model):
    genre_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='genre_section')
    content = models.TextField()
    genre_image = CloudinaryField('image', default='placeholder_ex9qjl.jpg')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.genre_name


class Band(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,
                              related_name='bands')
    band_name = models.CharField(max_length=80)
    band_email = models.EmailField()
    band_bio = models.TextField()
    band_image = CloudinaryField('image', default='placeholder_ex9qjl.jpg')
    next_gig = models.TextField(default='DD-MM-YYYY')
    concert_venue = models.CharField(max_length=30, default='TBA')
    status = models.IntegerField(choices=STATUS, default=0) 
    band_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.band_name