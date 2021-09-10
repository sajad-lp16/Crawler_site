from rest_framework import serializers
from comments.models import Comment
from accounts.api.serializers import UserSerializer
from movies.api.serializers import MovieSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'user',
            'movie',
            'content',
            'reply_to',
        )
