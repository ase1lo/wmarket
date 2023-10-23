from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    # 'third_name', 'first_name', 'second_name', 'status'
    username = models.CharField(_('Ник'), max_length=30, null=True)

    email = models.EmailField(_('Адрес электронной почты'), unique=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
    
