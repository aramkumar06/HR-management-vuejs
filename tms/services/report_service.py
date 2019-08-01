from tms.models import Earning, Book
from django.db import connection


def report_member(team_id=None, year=None, month=None):
    if team_id is None:
        return []

    if month is not None and year is not None:
        querying_book = Book.objects.filter(year__exact=year, month__exact=month).first()
        year_month_query = """
                    AND te.withdrawn_date BETWEEN DATE('%s') AND DATE('%s') + INTERVAL '23 HOUR' + INTERVAL '59 MINUTE' + INTERVAL '59 SECOND' 
                """ % (querying_book.start_date, querying_book.end_date)
    elif month is None and year is not None:
        year_month_query = " AND te.year = " + year
    else:
        querying_book = Book.objects.filter(status__exact='Active').first()
        year_month_query = """
                            AND te.withdrawn_date BETWEEN DATE('%s') AND DATE('%s') + INTERVAL '23 HOUR' + INTERVAL '59 MINUTE' + INTERVAL '59 SECOND' 
                        """ % (querying_book.start_date, querying_book.end_date)

    raw_query = """
      SELECT
          tu.username                        AS    username
        , COALESCE(summaries.earning_sum, 0) AS    earning_sum
      FROM tms_user AS tu
      LEFT JOIN (
        SELECT
            tu1.username AS username
          , SUM(te.cost) AS earning_sum        
        FROM
          tms_user AS tu1
        LEFT JOIN tms_earning AS te ON tu1.id = te.earned_by_id 
        WHERE te.deleted_at IS NULL
          AND tu1.team_id = %s
          %s
        GROUP BY tu1.username      
      ) summaries ON tu.username = summaries.username
      WHERE tu.deleted_at IS NULL
        AND tu.team_id = %s
      ORDER BY tu.id ASC
        ;
    """ % (team_id, year_month_query, team_id, )

    cursor = connection.cursor()
    cursor.execute(raw_query)
    members_earned = cursor.fetchall()

    ret = []
    summary = 0.0
    for earning in members_earned:
        ret.append({
            "username": earning[0],
            "cost": earning[1],
        })

        summary += earning[1]

    return ret, summary


def report_team(year=None, month=None):
    if month is not None and year is not None:
        querying_book = Book.objects.filter(year__exact=year, month__exact=month).first()
        year_month_query = """
                    AND te.withdrawn_date BETWEEN DATE('%s') AND DATE('%s') + INTERVAL '23 HOUR' + INTERVAL '59 MINUTE' + INTERVAL '59 SECOND' 
                """ % (querying_book.start_date, querying_book.end_date)
    elif month is None and year is not None:
        year_month_query = " AND te.year = " + year
    else:
        querying_book = Book.objects.filter(status__exact='Active').first()
        year_month_query = """
                            AND te.withdrawn_date BETWEEN DATE('%s') AND DATE('%s') + INTERVAL '23 HOUR' + INTERVAL '59 MINUTE' + INTERVAL '59 SECOND' 
                        """ % (querying_book.start_date, querying_book.end_date)

    raw_query = """
      SELECT
          tt.name                            AS name
        , COALESCE(summaries.earning_sum, 0) AS earning_sum
      FROM
        tms_team AS tt
      LEFT JOIN (
        SELECT
            tt1.id AS id
          , SUM(te.cost) AS earning_sum        
        FROM
          tms_earning AS te
        INNER JOIN tms_user AS tu ON te.earned_by_id = tu.id
        INNER JOIN tms_team AS tt1 ON tu.team_id = tt1.id 
        WHERE te.deleted_at IS NULL
          %s
        GROUP BY tt1.id
      ) summaries ON tt.id = summaries.id
      ORDER BY tt.id ASC
      ;
    """ % (year_month_query, )

    cursor = connection.cursor()
    cursor.execute(raw_query)
    teams_earned = cursor.fetchall()
    ret = []
    summary = 0.0
    for earning in teams_earned:
        ret.append({
            "team_name": earning[0],
            "cost": earning[1],
        })

        summary += earning[1]

    return ret, summary
