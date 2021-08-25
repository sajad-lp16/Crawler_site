from django.db import models
from lib.shared_models import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.core import validators

from .utils import functions


class Genre(BaseModel):
    title = models.CharField(_('title'),
                             max_length=30,
                             unique=True
                             )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Genre'
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')


class Movie(BaseModel):
    name = models.CharField(_('Name'),
                            max_length=30,
                            )

    genre = models.ForeignKey(Genre,
                              on_delete=models.CASCADE
                              )

    movie_type = models.CharField(_('Movie type'),
                                  max_length=20,
                                  blank=True
                                  )

    rating = models.FloatField(_('Rating'),
                               blank=True,
                               null=True
                               )

    movie_language = models.CharField(_('Language'),
                                      max_length=30,
                                      blank=True
                                      )

    production_year = models.IntegerField(_('Production Year'),
                                          validators=[
                                              validators.MinValueValidator(limit_value=1200)],
                                          blank=True,
                                          null=True
                                          )

    director = models.CharField(_('Director'),
                                max_length=40,
                                blank=True
                                )

    actors = models.CharField(_('Actors'),
                              max_length=200,
                              blank=True
                              )

    cover = models.ImageField(_('Cover'),
                              upload_to=functions.file_name_setter,
                              blank=True,
                              null=True
                              )

    description = models.TextField(_('Description'),
                                   blank=True
                                   )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Movie'
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')
        unique_together = [('name', 'genre', 'movie_type')]
