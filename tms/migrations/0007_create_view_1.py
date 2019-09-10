# Generated manually by abc on 2019-09-10 07:06

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0006_rewardlog'),
    ]

    operations = [
        migrations.RunSQL("""
        CREATE VIEW view_current_reward AS
            SELECT 
                tms_team.id                                 AS team_id
              , tms_team.name                               AS team_name
              , last_reward.rewarded_date                   AS last_rewarded_date
              , COALESCE(last_reward.initial_amount, 0)     AS initial_amount
              , COALESCE(current_earning.cost, 0)           AS current_earning
            FROM
              tms_team
              INNER JOIN LATERAL (
                SELECT
                    tms_rewardlog.rewarded_date
                  , tms_rewardlog.initial_amount
                FROM
                  tms_rewardlog
                WHERE tms_rewardlog.reward_type = 'team'
                  AND tms_rewardlog.taken_id = tms_team.id
                ORDER BY tms_rewardlog.rewarded_date DESC, tms_rewardlog.id DESC 
                limit 1
              ) last_reward ON TRUE
              INNER JOIN lateral (
                SELECT 
                    SUM(tms_earning.cost) AS cost
                FROM
                  tms_earning
                INNER JOIN tms_user ON tms_earning.earned_by_id = tms_user.id
                WHERE tms_earning.deleted_at IS NULL
                    AND tms_earning.approved_date IS NOT NULL
                    AND tms_earning.approved_by_id IS NOT NULL
                    AND tms_user.team_id = tms_team.id
                    AND tms_earning.withdrawn_date > last_reward.rewarded_date
            ) current_earning ON TRUE
            ORDER BY tms_team.id ASC
        ;""")
    ]
