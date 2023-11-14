from django.urls import path

from rest_framework.routers import DefaultRouter

from habit.apps import HabitConfig
from habit.views import HabitListView, HabitCreateView, HabitRetrieveAPIView, HabitDestroyAPIView, \
    HabitUpdateAPIView, HabitViewSet, UserHabitListView, PublicHabitListView

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')

urlpatterns = [path('habits/create/', HabitCreateView.as_view(), name='habits_create'),
               path('habits/list/', HabitListView.as_view(), name='habits_list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits_get'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits_update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habits_delete'),
    path('my-habits/', UserHabitListView.as_view(), name='user_habit_list'),
    path('public-habits/', PublicHabitListView.as_view(), name='public_habit_list'),
] + router.urls