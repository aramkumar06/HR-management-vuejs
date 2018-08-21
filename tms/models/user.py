from django.db import models
from django.contrib.auth.models import AbstractUser
from tms.models.role import Role
from tms.models.team import Team


class User(AbstractUser):
    name = models.CharField(max_length=20, null=False, help_text='')
    birthday = models.DateField(null=False, help_text='')
    address = models.CharField(max_length=50, null=False, help_text='')
    contact_number = models.CharField(max_length=50, null=False, help_text='')

    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL, help_text='')
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, help_text='')

    pass

