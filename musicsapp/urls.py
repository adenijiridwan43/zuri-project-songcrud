from django.urls import path
from . import views

#these are urls for my musicsapp 

urlpatterns = [
    path ('song/', views.Song_list.as_view()),
    path ('song/<int:pk>', views.Song_Detail.as_view()),
    path ('artiste/', views.Artiste_list.as_view()),
    path ('artiste/<int:pk>', views.Artiste_Detail.as_view()),
]