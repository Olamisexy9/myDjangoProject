from django.db import models

# Create your models here.

class Artiste (models.Model):
    artiste_id = models.CharField(max_Lenght=20)
    first_name = models.CharField(max_Lenght=50)
    last_name = models.CharField(max_Lenght=50)
    age = models.CharField(max_Lenght=20)


class Song (models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    song_id = models.CharField(max_Lenght=20)
    song_title = models.CharField(max_Lenght=400)
    date_released = models.CharField(max_Lenght=400)
    likes =models.CharField(max_Lenght=400)
    artiste_id = models.CharField(max_Lenght=400)

class Lyric (models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    lyric_id = models.CharField(max_Lenght=20)
    content = models.CharField(max_Lenght=400)
    song_id = models.CharField(max_Lenght=400)