from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .utils import functions
from .utils import validators


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'), max_length=150, unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator], error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'),
                                   )
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.'
    ), )
    bio = models.TextField(_('bio'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to=functions.rename_file)
    age = models.PositiveSmallIntegerField(_('age'), blank=True, null=True)
    phone_number = models.PositiveBigIntegerField(_('phone number'), validators=[validators.phone_number_validator],
                                                  null=True, blank=True, unique=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
