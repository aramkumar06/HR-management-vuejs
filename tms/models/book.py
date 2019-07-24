from django.db import models
from django.contrib.postgres.fields import ArrayField

from tms.models import User
"""
    for settlement
version 1
    year
    month
    weeks
    status
    booked_date
    done_by
version 2
    start_date
    end_end
"""


class Book(models.Model):
    year = models.IntegerField(null=False, help_text='booking year')
    month = models.IntegerField(null=False, help_text='booking month')
    STATUS_CALCULATED = 'Calculated'
    STATUS_ACTIVE = 'Activate'
    STATUS_CHOICES = (
        (STATUS_CALCULATED, 'Calculated'),
        (STATUS_ACTIVE, 'Active'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, help_text='active or calculated')
    weeks = ArrayField(models.IntegerField(), null=False, help_text='aggregation of week numbers for month')
    booked_date = models.DateTimeField(null=True, help_text='date when accounting month is finished')
    done_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, help_text='user who calculated whole')
    comments = models.TextField(max_length=1024, null=True, help_text='comments')
    start_date = models.DateField(null=False, help_text='working month start date')
    end_date = models.DateField(null=False, help_text='working month end date')

    pass

