from django.contrib import admin
from . import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = 'title', 'create_time', 'update_time'


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = 'name', 'rating', 'production_year'
