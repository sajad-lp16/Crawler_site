from django.shortcuts import render
from django.views import generic


class CommentList(generic.ListView):
    pass


class CommentCreate(generic.CreateView):
    pass


class CommentDetailView(generic.DetailView):
    pass


class CommentUpdate(generic.UpdateView):
    pass


class CommentDeleteView(generic.DeleteView):
    pass
