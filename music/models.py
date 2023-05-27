from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User


class Registration(models.Model):
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    conform_password = models.CharField(max_length=50, null=True)

    def __str__ (self):
        return self.username

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name    

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,null=True)
    audio_file = models.FileField(upload_to='songs/')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    fav = models.ManyToManyField(Registration, related_name='favorite_songs', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.id)])

class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    description = models.TextField()
    image=models.ImageField(null=True)

    def _str_(self):
        return self.name
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.user.username
    