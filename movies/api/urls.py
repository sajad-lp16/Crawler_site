from django.urls import path

from . import views

app_name = 'movies_api'

urlpatterns = [
    path('genre-list-create/', views.GenreListCreateAPI.as_view(), name='genre_list_create'),
    path('movie-list-create/', views.MovieListCreateAPI.as_view(), name='movies_list_create'),

    path('genre-ret-up-dest/<str:slug>/',
         views.GenreRetrieveUpdateDestroy.as_view(), name='genre_retrieve_update_destroy'),

    path('movie-ret-up-dest/<str:slug>/',
         views.MovieRetrieveUpdateDestroy.as_view(), name='movie_retrieve_update_destroy'),
]
