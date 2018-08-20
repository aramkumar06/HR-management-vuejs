from django.db import models

"""
TODO
version 1
    reference to country
    reference to user
    email
    email_password
    skype
    skype_password
    status active or suspended
    phone_number

version 2
    title
    avatar
"""


class Account(models.Model):
    first_name = models.CharField(max_length=15, blank=False, help_text='')
    last_name = models.CharField(max_length=15, blank=False, help_text='')

    pass
