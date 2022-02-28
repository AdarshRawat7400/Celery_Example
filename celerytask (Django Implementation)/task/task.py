import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task
from faker import Faker

@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        faker = Faker()
        User.objects.create_user(
            first_name= "{}".format(get_random_string(length=5, allowed_chars=string.ascii_letters)),
            last_name="{}".format(get_random_string(length=5, allowed_chars=string.ascii_letters)),
            username=faker.name(),
            email=faker.email(),
            password=get_random_string(length=10),
        )
    return '{} random users created with success!'.format(total)
