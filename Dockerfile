# Dockerfile для Django
FROM python:3

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Устанавливаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=config.settings.production

# Применяем миграции
RUN python manage.py migrate

# Запускаем Django приложение
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
