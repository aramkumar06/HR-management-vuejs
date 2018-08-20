from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=30, blank=False, help_text='')
    url = models.CharField(max_length=100, blank=False, help_text='')
    description = models.TextField(max_length=5000, blank=True, help_text='')

    pass
