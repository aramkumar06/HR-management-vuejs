from django.db import models

from tms.models.project import Project


class Earning(models.Model):
    cost = models.FloatField(null=False, help_text='')
    start_week_date = models.DateField(null=False, help_text='Start date of week')
    end_week_date = models.DateField(null=False, help_text='End date of week')
    week_of_year = models.IntegerField(null=False, help_text='')
    month_of_year = models.IntegerField(null=False, help_text='')
    year = models.IntegerField(null=False, help_text='')
    week_year = models.CharField(max_length=7, null=False, help_text='EX: 2018-48')
    updated_date = models.DateTimeField(auto_now_add=True, help_text='')
    registered_date = models.DateTimeField(auto_now_add=True, help_text='')
    STATUS_PENDING = 'PD'
    STATUS_BALANCE = 'BL'
    STATUS_WITHDRAW = 'WD'
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_BALANCE, 'Balance'),
        (STATUS_WITHDRAW, 'Withdraw'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_PENDING, help_text='')
    approved_date = models.DateTimeField(null=True, help_text='Date Time when confirm balance')
    withdrawn_date = models.DateTimeField(null=True, help_text='Date Time when withdraw')

    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, help_text='')

    pass
