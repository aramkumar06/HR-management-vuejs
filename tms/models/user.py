from django.db import models
from django.contrib.auth.models import AbstractUser
from tms.models.role import Role
from tms.models.team import Team
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=20, blank=False, help_text='')
    birthday = models.DateField(blank=False, help_text='')
    address = models.CharField(max_length=50, blank=False, help_text='')
    contact_number = models.CharField(max_length=50, blank=False, help_text='')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, help_text='')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, help_text='')

    pass

