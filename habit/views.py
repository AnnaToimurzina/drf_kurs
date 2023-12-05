from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habit.models import Habit
from habit.paginator import MyPagination
from habit.permissions import IsOwnerOrReadOnly, ReadOnlyIfPublic

from habit.serializer import HabitSerializer
from .tasks import send_reminder_email


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit_instance = serializer.save(user=self.request.user)  # Сохранение владельца при создании объекта
        send_reminder_email.delay(self.request.user.email, habit_instance.name_habit)



class HabitListView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = MyPagination

class UserHabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

class PublicHabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [AllowAny, ReadOnlyIfPublic]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)




class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def healthcheck(request):
    return JsonResponse({'status': 'ok'})




