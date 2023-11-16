from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

from celery import shared_task
from celery.schedules import crontab
from django.utils import timezone

from config.celery import app
from .models import Habit
from django.contrib.auth.models import User
from django.core.mail import send_mail
from telegram import Bot

@shared_task
def send_reminder_email(user_email, user_id, habit_name):
    # Логика для отправки напоминания на почту
    send_mail(
        'Reminder',
        f"Don't forget to complete your habit: {habit_name}",
        'from@example.com',
        [user_email],
        fail_silently=False,
    )

    # Отправка напоминания через Telegram
    bot_token = os.getenv('BOT_TOKEN')
    bot = Bot(token=bot_token)

    user = User.objects.get(pk=user_id)
    chat_id = user.telegram_chat_id  # Предполагается, что у пользователя есть поле telegram_chat_id
    bot.send_message(chat_id, f"Don't forget to complete your habit: {habit_name}")


@shared_task
def check_and_send_reminders():
    # Логика для проверки привычек и отправки напоминаний
    habits = Habit.objects.filter(
        time__lte=timezone.now(),
        is_completed=False,
    )

    for habit in habits:
        user_email = habit.user.email
        habit_name = habit.name_habit
        send_reminder_email.delay(user_email, habit_name)

app.conf.beat_schedule = {
    'check-and-send-reminders': {
        'task': 'habit.tasks.check_and_send_reminders',
        'schedule': crontab(minute=0, hour=15),  # Каждый день в 15:00
    },
}

app.conf.timezone = 'UTC'