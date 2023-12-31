from django.db import models

from config import settings
from location.models import Location
from time_location.models import Time
from users.models import User

class Habit(models.Model):

    name_habit = models.CharField(max_length=100)  # Название привычки
    description_habit = models.TextField(blank=True, null=True)  # Описание привычки
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)  # Действие, которое представляет из себя привычку
    is_pleasurable = models.BooleanField(default=False)  # Признак приятной привычки
    periodicity = models.PositiveIntegerField(default=1)  # Периодичность выполнения привычки (по умолчанию ежедневная)
    reward = models.CharField(max_length=200)  # Чем пользователь должен себя вознаградить после выполнения
    estimated_time = models.PositiveIntegerField()  # Время, которое предположительно потратит пользователь на выполнение привычки
    is_public = models.BooleanField(default=False)  # Признак публичности привычки (можно ли публиковать в общий доступ)
    linked_habits = models.ManyToManyField('self', blank=True, symmetrical=False)  # связанная привычка

    def __str__(self):
        return f"{self.user} - {self.name_habit}"

    class Meta:
        verbose_name = 'Привычки'
        verbose_name_plural = 'Привычки'
