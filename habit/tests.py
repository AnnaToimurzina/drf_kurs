from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from users.models import User
from .models import Habit


class HabitCRUDTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test_anna@test.ru') # Создаем пользователя
        self.user.set_password('test')
        self.user.save()


    def test_create_habit(self):
        url = reverse('habit:habits_create')
        data = {
            'name_habit': 'TestHabit',
                'description_habit': 'Test habit description',
                'user': self.user.id,
                'action': 'Test action',
                'is_pleasurable': True,
                'periodicity': 1,
                'reward': 'Test reward',
                'estimated_time': 30,
                'is_public': False,
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.first().name_habit, 'TestHabit')

    def test_user_habit_list_view(self):
        url = reverse('habit:user_habit_list')


        habit1 = Habit.objects.create(
            name_habit='Habit1',
            description_habit='Description 1',
            user=self.user,
            action='Action 1',
            is_pleasurable=True,
            periodicity=1,
            reward='Reward 1',
            estimated_time=30,
            is_public=False,)

        habit2 = Habit.objects.create(
            name_habit='Habit2',
            description_habit='Description 2',
            user=self.user,
            action='Action 2',
            is_pleasurable=True,
            periodicity=1,
            reward='Reward 2',
            estimated_time=30,
            is_public=False,
        )

        self.client.force_authenticate(user=self.user)
        data = {'habit1': habit1.id, 'habit2': habit2.id}
        response = self.client.get(url, data=data)


        # Проверка успешного ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка, что привычки пользователя присутствуют в ответе
        self.assertEqual(len(response.data), 2)
















