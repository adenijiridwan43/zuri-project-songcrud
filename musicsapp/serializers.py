from rest_framework import serializers
from .models import Artiste, Song

class Artisteserializers(serializers.ModelSerializer) :
    class Meta:
        model = Artiste
        fields = ['first_name','second_name','age']


class Songserializers (serializers.ModelSerializer) :
    class Meta:
        model = Song
        fields = ['title', 'date_release', 'likes', 'artiste_id']

