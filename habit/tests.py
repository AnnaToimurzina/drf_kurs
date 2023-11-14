from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Habit

User = get_user_model()

class HabitViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test_user@test.com',
            password='test_password'
        )
        self.client = APIClient()

    def test_list_habits(self):
        # Создаем привычку
        habit = Habit.objects.create(
            title='Test Habit',
            description='Test description',
            user=self.user
        )

        url = reverse('habit-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_habit(self):
        url = reverse('habit-list')
        data = {
            'title': 'New Habit',
            'description': 'New habit description',
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.first().title, 'New Habit')

    def test_retrieve_habit(self):
        # Создаем привычку
        habit = Habit.objects.create(
            title='Test Habit',
            description='Test description',
            user=self.user
        )

        url = reverse('habit-detail', args=[habit.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Habit')

    def test_update_habit(self):
        # Создаем привычку
        habit = Habit.objects.create(
            title='Test Habit',
            description='Test description',
            user=self.user
        )

        url = reverse('habit-detail', args=[habit.id])
        data = {
            'title': 'Updated Habit',
            'description': 'Updated habit description',
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.first().title, 'Updated Habit')

    def test_delete_habit(self):
        # Создаем привычку
        habit = Habit.objects.create(
            title='Test Habit',
            description='Test description',
            user=self.user
        )

        url = reverse('habit-detail', args=[habit.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
