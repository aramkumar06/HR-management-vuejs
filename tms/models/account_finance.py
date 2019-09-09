from django.db import models

from tms.models import Account
class AccountFinance(models.Model):
    financial_account = models.ForeignKey(Account, related_name='financial_account', null=False, on_delete=models.CASCADE, help_text='financial account')
    email_account = models.ForeignKey(Account, related_name='email_account',null=False, on_delete=models.CASCADE,help_text='email account mapped')
    deleted_at = models.DateTimeField(null=True, help_text='date when deleted')
