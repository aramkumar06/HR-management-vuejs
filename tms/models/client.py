from django.db import models

from tms.models.country import Country
from tms.models.account import Account
from tms.models.site import Site
"""
version 1
    first name
    last name
    email
    skype
    phone number
    reference url
    refer to country
    refer to account
    refer to site 
version 2
    avatar
"""


class Client(models.Model):
    first_name = models.CharField(max_length=15, blank=False, help_text='')
    last_name = models.CharField(max_length=15, blank=False, help_text='')
    email = models.CharField(max_length=30, blank=True, help_text='Email address of client')
    skype = models.CharField(max_length=30, blank=True, help_text='Skype username of client')
    phone_number = models.CharField(max_length=11, blank=True, help_text='Phone number of client')
    url = models.CharField(max_length=100, blank=True, help_text='Reference URL')
    country = models.ForeignKey(Country, blank=True, help_text='')
    account = models.ForeignKey(Account, blank=True, help_text='')
    site = models.ForeignKey(Site, blank=True, help_text='')

    pass
