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
    registered date
    recital
    refer to country
    refer to account
    refer to site 
version 2
    avatar
"""


class Client(models.Model):
    first_name = models.CharField(max_length=15, blank=False, help_text='')
    last_name = models.CharField(max_length=15, blank=False, help_text='')
    email = models.EmailField(max_length=30, blank=True, help_text='Email address of client')
    skype = models.CharField(max_length=30, blank=True, help_text='Skype username of client')
    phone_number = models.CharField(max_length=11, blank=True, help_text='Phone number of client')
    url = models.URLField(max_length=100, blank=True, help_text='Reference URL')
    recital = models.TextField(max_length=1000, blank=True, help_text='Explain his attitude and other experiences.')
    registered_date = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, blank=True, on_delete=models.SET_NULL, help_text='')
    account = models.ForeignKey(Account, blank=True, on_delete=models.SET_NULL, help_text='')
    site = models.ForeignKey(Site, blank=True, on_delete=models.SET_NULL, help_text='')

    pass
