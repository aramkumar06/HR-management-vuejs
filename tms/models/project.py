from django.db import models

from tms.models.account import Account
from tms.models.client import Client

"""
version 1
    title
    description
    start_date
    end_date
    status
    project_type
    price
    limit
    posted_datetime
    applied_datetime
    applied_proposals_count
    interview_count
    registered date
    refer to account
    refer to client
version 2
    tags
"""


class Project(models.Model):
    title = models.CharField(max_length=30, blank=False, help_text='')
    description = models.TextField(max_length=1000, blank=False, help_text='')
    start_date = models.DateField(blank=False, help_text='Project start date')
    end_date = models.DateField(blank=True, help_text='Project end date')
    STATUS_STARTED = 'ST'
    STATUS_ENDED = 'EN'
    STATUS_DISPUTED = 'DS'
    STATUS_CHOICES = (
        (STATUS_STARTED, 'Start'),
        (STATUS_ENDED, 'End'),
        (STATUS_DISPUTED, 'Dispute'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_STARTED)
    JOB_HOURLY = 'HR'
    JOB_FIXED = 'FX'
    JOB_CHOICES = (
        (JOB_HOURLY, 'Hourly'),
        (JOB_FIXED, 'Fixed'),
    )
    project_type = models.CharField(max_length=2, choices=JOB_CHOICES, default=JOB_FIXED)
    price = models.FloatField(blank=False, help_text='Fixed price of project or hourly rate of project')
    limit = models.IntegerField(blank=True, help_text='')
    posted_datetime = models.DateTimeField(blank=True, help_text='Date and Time when the job is posted')
    applied_datetime = models.DateTimeField(blank=True, help_text='Date and Time when applying for job')
    applied_proposals_count = models.IntegerField(blank=True, help_text='Total proposals when hiring')
    interview_count = models.IntegerField(blank=True, help_text='Total interview count when hiring')
    registered_date = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL)

    pass
