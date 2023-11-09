from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    client = models.CharField(max_length=100, verbose_name='Full name')
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username} {self.email} {self.password}"

    class Meta:
        verbose_name = 'Создатель привычки'
        verbose_name_plural = 'Создатель привычки'
