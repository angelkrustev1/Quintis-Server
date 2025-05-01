from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        permissions = [
            ('can_administer_profiles', 'Can administer all profiles'),
        ]

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    profile_url = models.URLField(
        null=True,
    )

    data_joined = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()

    EMAIL_FIELD = 'email',
    USERNAME_FIELD = 'email',
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.email}'



