from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('movies-list/<str:slug>/', views.MoviesList.as_view(), name='movies_list'),
    path('<str:slug1>/movie-detail/<str:slug>/', views.MovieDetail.as_view(), name='movie_detail'),
]
