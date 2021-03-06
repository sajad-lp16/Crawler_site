from django.shortcuts import get_object_or_404
from django.views import generic

from . import models
from comments.models import Comment


class Home(generic.ListView):
    model = models.Movie
    template_name = 'home.html'
    context_object_name = 'movies'
    paginate_by = 18


class MoviesList(generic.ListView):
    paginate_by = 18
    template_name = 'home.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return models.Movie.objects.filter(genre__slug=self.kwargs['slug'])


class MovieDetail(generic.DetailView):
    model = models.Movie
    template_name = 'movie_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(models.Movie, slug=self.kwargs['slug'], genre__slug=self.kwargs['slug1'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.get_comments(self.get_object().id)
        return context
