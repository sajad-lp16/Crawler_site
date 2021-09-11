from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

User = get_user_model()


class AuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return
        user = User.objects.filter(
            Q(username=username) | Q(email=username)
        ).first()
        if user is None:
            try:
                user = User.objects.filter(phone_number=username).first()
            except ValueError:
                return

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
