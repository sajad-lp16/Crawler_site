from django.contrib import admin

from . import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
