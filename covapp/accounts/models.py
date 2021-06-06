from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .country import all_country_code_dict
from rest_framework.authtoken.models import Token

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, firstname, lastname, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname, lastname=lastname, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, firstname, lastname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, firstname, lastname, password, **extra_fields)

    def create_superuser(self, email, firstname, lastname, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, firstname, lastname, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    firstname = models.CharField(verbose_name='First Name',
                               max_length=20,
                               unique=False)
    lastname = models.CharField(verbose_name='Last Name',
                               max_length=20,
                               unique=False)

    countries_as_list = [(k, v) for k, v in all_country_code_dict.items()]
    country = models.CharField(verbose_name='Country',
                               max_length=50,
                               choices=countries_as_list)
    REQUIRED_FIELDS = ['firstname', 'lastname', 'country']
    objects = CustomUserManager()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)