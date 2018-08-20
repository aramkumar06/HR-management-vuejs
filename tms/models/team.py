from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=20, help_text='')
    description = models.CharField(max_length=100, blank=True, help_text='')

    pass
