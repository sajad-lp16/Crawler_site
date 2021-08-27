from django.contrib import admin
from . import models


class MovieInline(admin.TabularInline):
    model = models.Movie


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = 'title', 'create_time', 'update_time'
    inlines = [MovieInline]


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = 'name', 'rating', 'production_year', 'director'
    search_fields = 'name', 'director', 'genre'
    list_filter = 'genre',
    list_editable = 'director', 'rating', 'production_year'
