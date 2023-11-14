from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    subject = 'Welcome to My Site'
    message = 'Thank you for signing up. We appreciate your business.'
    from_email = 'webmaster@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)