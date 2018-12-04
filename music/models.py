from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your models here.

class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title + "-" + self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title=models.CharField(max_length=250)
    #is_favorite=models.BooleanField(default=False)

    def get_absolute_url(self):
        #album_id = Album.objects.get(self.album=Album.album_title).id  # Experiment with album_title, album=album
        return reverse('music:detail',kwargs={'pk':self.album.primary_key})

    def __str__(self):
        return self.song_title