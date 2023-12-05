# Dockerfile для Django
FROM python:3

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Устанавливаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=config.settings.production

# Запускаем Django приложение
CMD ["bash", "-c", "wait-for-it.sh db:5432 -- python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]

