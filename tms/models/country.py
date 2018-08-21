from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30, null=False, help_text='')
    code = models.CharField(max_length=2, null=False, help_text='')

    pass
