from django.db import models

class RewardLog(models.Model):
    REWARD_TEAM = 'team'
    REWARD_MEMBER = 'member'
    REWARD_DELEGATION = 'delegation'
    REWARD_TYPES_CHOICES = (
        (REWARD_TEAM, 'team'),
        (REWARD_MEMBER, 'member'),
        (REWARD_DELEGATION, 'delegation'),
    )
    reward_type = models.CharField(max_length=32, null=False, help_text='reward type')
    taken_id = models.IntegerField(null=False, help_text='id of taken. team_id when "team", user_id when "member"')
    rewarded_date = models.DateField(null=False, help_text='rewarded date')
    initial_amount = models.FloatField(null=False, help_text='the remaining amount after rewarding')
