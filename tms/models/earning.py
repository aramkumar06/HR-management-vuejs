from django.db import models

from tms.models import Account
from tms.models import Client
from tms.models import Project
from tms.models import User


class Earning(models.Model):
    cost = models.FloatField(null=False, help_text='')
    start_week_date = models.DateField(null=False, help_text='Start date of week')
    end_week_date = models.DateField(null=False, help_text='End date of week')
    week_of_year = models.IntegerField(null=False, help_text='')
    month_of_year = models.IntegerField(null=False, help_text='')
    year = models.IntegerField(null=False, help_text='')
    # week_year = models.CharField(max_length=7, null=False, help_text='EX: 2018-48')
    updated_date = models.DateTimeField(auto_now_add=True, help_text='')
    registered_date = models.DateTimeField(auto_now_add=True, help_text='')
    confirmed = models.BooleanField(null=True, default=False, help_text='Confirm paying')
    # STATUS_PENDING = 'PD'
    # STATUS_BALANCE = 'BL'
    # STATUS_WITHDRAW = 'WD'
    # STATUS_FEE = 'FE'
    # STATUS_RF = 'RF'
    # STATUS_CHOICES = (
    #     (STATUS_PENDING, 'Pending'),
    #     (STATUS_BALANCE, 'Balance'),
    #     (STATUS_WITHDRAW, 'Withdraw'),
    #     (STATUS_FEE, 'Fee'),
    #     (STATUS_RF, 'Refund'),
    # )
    # EARN_TYPE_GET = 'GT'
    # EARN_TYPE_FEE = 'FE'
    # EARN_TYPE_REFUND = 'RF'
    # EARN_TYPE_CHOICES = (
    #     (EARN_TYPE_GET, 'Get'),
    #     (EARN_TYPE_FEE, 'Fee'),
    #     (EARN_TYPE_REFUND, 'Refund'),
    # )
    # earn_type = models.CharField(max_length=2, choices=EARN_TYPE_CHOICES, default=EARN_TYPE_GET, help_text='')
    # status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_PENDING, help_text='')
    approved_date = models.DateTimeField(null=True, help_text='Date Time when confirm balance')
    withdrawn_date = models.DateTimeField(null=True, help_text='Date Time when withdraw')

    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, help_text='used when calculating per project')
    approved_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, help_text='user who confirmed paying')
    # account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, help_text='used when calculating per account')
    # client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL, help_text='used when calculating per client')
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, help_text='used when calculating per user')

    pass
