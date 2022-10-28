from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.

class Artiste (models.Model) :
    # A class name for Artist profile sit here

    first_name = models.CharField( max_length=200)
    second_name = models.CharField( max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song (models.Model) :
    # A class name for Song profile sit here
    title = models.CharField( max_length=200)
    date_release = models.DateField( default=datetime.today)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
            return self.title


class Lyrics (models.Model) : 
    # A class name for Lyrics profile sit here
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content