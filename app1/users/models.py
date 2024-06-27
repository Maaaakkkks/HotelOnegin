from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    
