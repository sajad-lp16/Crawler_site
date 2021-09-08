from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'avatar',
            'bio',
            'phone_number',
            'age',
        )

        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
        }

    def to_representation(self, instance):
        request = self.context['request']
        data = super().to_representation(instance)
        if request.user != instance:
            data.pop('is_staff')
            data.pop('is_active')
            data.pop('email')
            data.pop('phone_number')
            return data
        Token.objects.get_or_create(user=instance)
        data['token'] = instance.auth_token.key
        return data
