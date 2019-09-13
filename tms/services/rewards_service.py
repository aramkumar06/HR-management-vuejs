import os
import datetime

from django.db import connection

from tms.models import RewardLog

def get_teams_rewards():
    reward_team_threshold = int(os.getenv('REWARD_TEAM_THRESHOLD'))
    raw_query = """
        SELECT 
            tms_team.id
          , tms_team.name
          , last_reward.rewarded_date
          , COALESCE(last_reward.initial_amount, 0)
          , COALESCE(current_earning.cost, 0)
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
            LIMIT 1
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
    ;"""

    cursor = connection.cursor()
    cursor.execute(raw_query)
    teams_reward = cursor.fetchall()

    ret = []
    for reward in teams_reward:
        ret.append({
            'team_id': reward[0],
            'team_name': reward[1],
            'rewarded_date': reward[2],
            'initial_amount': float(format(reward[3], '.2f')),
            'cost': float(format(reward[4], '.2f')),
            'can_reward': int(reward[3] + reward[4]) >= reward_team_threshold
        })

    return ret

def award_bonus_team(team_id=None):
    if team_id is None:
        return False

    reward_team_threshold = int(os.getenv('REWARD_TEAM_THRESHOLD'))
    raw_query = """
        SELECT 
            tms_team.id
          , tms_team.name
          , last_reward.rewarded_date
          , COALESCE(last_reward.initial_amount, 0)
          , COALESCE(current_earning.cost, 0)
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
            ORDER BY rewarded_date DESC, tms_rewardlog.id DESC
            LIMIT 1
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
        WHERE tms_team.id = %s
        ORDER BY tms_team.id ASC
    ;""" % (team_id, )

    cursor = connection.cursor()
    cursor.execute(raw_query)
    last_reward = cursor.fetchone()

    initial_amount = float(last_reward[3])
    current_earning = float(last_reward[4])

    if initial_amount + current_earning < reward_team_threshold:
        return False

    next_initial_amount = float(format(initial_amount + current_earning - reward_team_threshold, '.2f'))

    reward = RewardLog(reward_type=RewardLog.REWARD_TEAM, taken_id=team_id, rewarded_date=datetime.datetime.utcnow(), initial_amount=next_initial_amount)
    reward.save()

    return True

def get_current_team_reward(team_id=None):
    if not team_id:
        return None

    raw_query = """
      SELECT
          view_current_reward.team_id
        , view_current_reward.team_name
        , view_current_reward.last_rewarded_date
        , view_current_reward.initial_amount
        , view_current_reward.current_earning
      FROM
        view_current_reward
      WHERE view_current_reward.team_id = %s
    """ % (team_id, )

    cursor = connection.cursor()
    cursor.execute(raw_query)
    team_reward = cursor.fetchone()

    last_reward_date = team_reward[2]
    initial_amount = float(format(team_reward[3], '.2f'))
    current_earning = float(format(team_reward[4], '.2f'))

    threshold = int(os.getenv('REWARD_TEAM_THRESHOLD'))
    mission = threshold - initial_amount - current_earning
    ret = {
        'last_reward_date': last_reward_date,
        'initial_amount': initial_amount,
        'current_earning': current_earning,
        'mission': mission,
    }

    return ret
