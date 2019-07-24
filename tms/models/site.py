from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=30, null=False, help_text='')
    url = models.URLField(max_length=100, null=False, help_text='')
    description = models.TextField(max_length=1024, null=True, help_text='')

    pass
