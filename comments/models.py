from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.shared_models import BaseModel
from movies.models import Movie

User = get_user_model()


class CommentManager(models.Manager):
    def get_comments(self, pk):
        return self.filter(movie_id=pk, status=True, reply_to=None)


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name=_('user'))
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments', verbose_name=_('movie'))
    content = models.TextField(verbose_name=_('content'))
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE,
                                 related_name='replies', verbose_name=_('replies'), null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name=_('status'))

    objects = CommentManager()

    def __str__(self):
        return f'{self.user} -> {self.movie.name}'

    class Meta:
        db_table = 'Comments'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
