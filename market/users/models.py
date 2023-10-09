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
    
    # def get_absolute_url(self):
    #     return "/users/profile/%i" % self.id


# class Follower(models.Model):
#     follower = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, related_name='Подписчик')
#     author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, related_name='Автор')
#     #можно подписаться несколько раз