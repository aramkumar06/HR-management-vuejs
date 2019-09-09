from django.db import models

from tms.models import Account
from tms.models import User

class Earning(models.Model):
    cost = models.FloatField(null=False, help_text='')
    year = models.IntegerField(null=False, help_text='')
    STATUS_WITHDRAW = 'Withdraw'
    STATUS_CHOICES = (
        (STATUS_WITHDRAW, 'Withdraw'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_WITHDRAW, help_text='')
    withdrawn_date = models.DateField(null=True, help_text='date time when withdraw')
    comments = models.TextField(max_length=1024, null=True, help_text='description')
    created_at = models.DateField(auto_now_add=True, null=False, help_text='created date')
    deleted_at = models.DateTimeField(null=True, help_text='deleted date')
    earned_by = models.ForeignKey(User, related_name='earned_by', null=True, on_delete=models.SET_NULL, help_text='user who earns')
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, help_text='mapped to account')
    approved_date = models.DateField(null=True, help_text='date when approved')
    approved_by = models.ForeignKey(User, related_name='approved_by', null=True, on_delete=models.SET_NULL, help_text='user who confirmed paying')
    finance_account = models.ForeignKey(Account, related_name='finance_account', null=True, on_delete=models.SET_NULL, help_text='actual financial account')

    pass
