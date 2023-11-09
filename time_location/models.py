from django.db import models

class Time(models.Model):
    name_time = models.CharField(max_length=100)  # Название времени (например, "Утро", "Вечер")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_time, self.description

    class Meta:
        verbose_name = 'Время суток'
        verbose_name_plural = 'Время суток'