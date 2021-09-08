from rest_framework import generics

from movies.utils import functions
from movies import models
from .custom_pagination import SmallPagination
from . import serializers


class GenreListCreateAPI(generics.ListCreateAPIView):
    serializer_class = serializers.GenreSerializer
    queryset = models.Genre.objects.all()
    pagination_class = SmallPagination


class GenreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GenreSerializer
    queryset = models.Genre.objects.all()
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class MovieListCreateAPI(generics.ListCreateAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.all()
    pagination_class = SmallPagination

    def perform_create(self, serializer):
        name = serializer.validated_data['name']
        slug = functions.generate_slug(name)
        serializer.save(slug=slug)


class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.all()
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'
