from rest_framework import generics

from comments.models import Comment
from . import serializers
from ..utils.permissions import CommentOwnerPermission


class CommentListCreateAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = CommentOwnerPermission,

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, movie_id=self.request.data['pk'])


class CommentRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    serializer_class = serializers.CommentSerializer
    permission_classes = CommentOwnerPermission,
    queryset = Comment.objects.all()
