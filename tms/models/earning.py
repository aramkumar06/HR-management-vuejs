from django.db import models

from tms.models import Project
from tms.models import User


class Earning(models.Model):
    cost = models.FloatField(null=False, help_text='')
    week_of_year = models.IntegerField(null=False, help_text='')
    year = models.IntegerField(null=False, help_text='')
    updated_date = models.DateTimeField(auto_now_add=True, help_text='')
    registered_date = models.DateTimeField(auto_now_add=True, help_text='')
    STATUS_PENDING = 'PD'
    STATUS_BALANCE = 'BL'
    STATUS_WITHDRAW = 'WD'
    STATUS_FEE = 'FE'
    STATUS_RF = 'RF'
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_BALANCE, 'Balance'),
        (STATUS_WITHDRAW, 'Withdraw'),
        (STATUS_FEE, 'Fee'),
        (STATUS_RF, 'Refund'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_PENDING, help_text='')
    approved_date = models.DateTimeField(null=True, help_text='Date Time when confirm balance')
    withdrawn_date = models.DateTimeField(null=True, help_text='Date Time when withdraw')
    comments = models.TextField(max_length=1024, null=True, help_text='Add comments here')
    deleted_at = models.DateTimeField(null=True, help_text='deleted date')

    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, help_text='used when calculating per project')
    approved_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, help_text='user who confirmed paying')

    pass
