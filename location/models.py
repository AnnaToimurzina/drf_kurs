from django.db import models


class Location(models.Model):
    name_location = models.CharField(max_length=100)  # Название места
    description_location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_location, self.description_location


    class Meta:
        verbose_name = 'Название места'
        verbose_name_plural = 'Название места'



