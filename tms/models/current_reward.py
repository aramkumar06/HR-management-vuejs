from django.db import models

class CurrentReward(models.Model):
    team_id = models.IntegerField(null=False, help_text='team id')
    team_name = models.CharField(null=False, max_length=20, help_text='team name')
    last_rewarded_date = models.DateField(null=False, help_text='last rewarded date')
    initial_amount = models.FloatField(null=False, help_text='remaining amount after calculation')
    current_earning = models.FloatField(null=False, help_text='sum of earned cost after last rewarding')
    class Meta:
        managed = False
        db_table = 'view_current_reward'
