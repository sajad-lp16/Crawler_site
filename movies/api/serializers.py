from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from movies import models

from movies.utils import functions


class GenreSerializer(serializers.ModelSerializer):
    serializers.HyperlinkedModelSerializer()

    class Meta:
        model = models.Genre
        fields = (
            'title',
            'slug',
        )
        extra_kwargs = {
            'title': {'validators': []},
            'slug': {'read_only': True},
        }

    def create(self, validated_data):
        title = validated_data['title']
        slug = functions.generate_slug(title)
        instance, _ = models.Genre.objects.get_or_create(title=title, slug=slug)
        return instance


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = models.Movie
        fields = (
            'name',
            'slug',
            'genre',
            'movie_type',
            'rating',
            'movie_language',
            'production_year',
            'director',
            'actors',
            'cover',
            'description',
        )

        extra_kwargs = {
            'slug': {'read_only': True},
        }

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        genre, _ = models.Genre.objects.get_or_create(**genre)
        instance = models.Movie.objects.create(**validated_data, genre=genre)
        return instance

    # Custom method to handle nested genre update
    def update(self, instance, validated_data):
        genre = validated_data.pop('genre')
        genre, _ = models.Genre.objects.get_or_create(**genre)

        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        m2m_fields = []

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)
        instance.genre = genre
        instance.save()

        return instance
