from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from celery import shared_task

@shared_task
def mail_sender(subject,body):
    message = f'''
Hi {body['first_name']} {body['last_name']},
    
    {body['message']}

Regards,
adarshrawat71@gmail.com

    '''
    try:
        send_mail(subject, message, 'adarshrawat71@gmail.com', [body['email']]) 
    except BadHeaderError:
        return False
    return True