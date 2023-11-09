from django.db import models

from location.models import Location
from time_location.models import Time
from users.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Создатель привычки
    name_habit = models.CharField(max_length=100)  # Название привычки
    description_habit = models.TextField(blank=True, null=True)  # Описание привычки
    name_location = models.ForeignKey(Location, on_delete=models.CASCADE)  # Место, где нужно выполнять привычку
    name_time = models.ForeignKey(Time, on_delete=models.CASCADE)  # Время, когда нужно выполнять привычку
    action = models.CharField(max_length=200)  # Действие, которое представляет из себя привычку
    is_pleasurable = models.BooleanField(default=False)  # Признак приятной привычки
    periodicity = models.PositiveIntegerField(default=1)  # Периодичность выполнения привычки (по умолчанию ежедневная)
    reward = models.CharField(max_length=200)  # Чем пользователь должен себя вознаградить после выполнения
    estimated_time = models.PositiveIntegerField()  # Время, которое предположительно потратит пользователь на выполнение привычки
    is_public = models.BooleanField(default=False)  # Признак публичности привычки (можно ли публиковать в общий доступ)
    linked_habits = models.ManyToManyField('self', blank=True)  # Список связанных привычек

    def __str__(self):
        return self.user, self. name_habit, self.description_habit, self.name_location, self.name_time, self.action, self.is_pleasurable, self.periodicity, self.reward, self.estimated_time, self.is_public, self.linked_habits

    class Meta:
        verbose_name = 'Привычки'
        verbose_name_plural = 'Привычки'
