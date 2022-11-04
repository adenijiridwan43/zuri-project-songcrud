from django.shortcuts import render
from .models import Artiste, Song, Lyrics
from .serializers import Artisteserializers, Songserializers
from rest_framework import generics

# Create your views here.

class Artiste_list(generics.ListCreateAPIView) :
    queryset = Artiste.objects.all()
    serializer_class = Artisteserializers

class Artiste_Detail (generics.RetrieveUpdateDestroyAPIView) :
    queryset = Artiste.objects.all()
    serializer_class = Artisteserializers


class Song_list(generics.ListCreateAPIView) :
    queryset = Song.objects.all()
    serializer_class = Songserializers

class Song_Detail (generics.RetrieveUpdateDestroyAPIView) :
    queryset = Song.objects.all()
    serializer_class = Songserializers
