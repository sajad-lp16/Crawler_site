from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers
from accounts.utils.permissions import UserOwnerPermission

User = get_user_model()


class UserListCreateAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        serializer.save(password=make_password(password))


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    permission_classes = UserOwnerPermission,
    authentication_classes = TokenAuthentication,

    def perform_update(self, serializer):
        password = serializer.initial_data.get('password')
        if password is not None:
            serializer.save(password=make_password(password))
        else:
            serializer.save()
