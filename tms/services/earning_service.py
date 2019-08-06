from tms.models import Earning, Book


def get_earnings(account_id=None, year=None, month=None, user_id=None):
    if account_id is not None:
        account_query = " AND ta.id = " + account_id
    else:
        account_query = ""

    if year is not None:
        year_query = " AND te.year = " + year
    else:
        year_query = ""

    if month is not None and year is not None:
        querying_book = Book.objects.filter(year__exact=year, month__exact=month).first()
        month_query = """
            AND te.withdrawn_date BETWEEN DATE('%s') AND DATE('%s') + INTERVAL '23 HOUR' + INTERVAL '59 MINUTE' + INTERVAL '59 SECOND' 
        """ % (querying_book.start_date, querying_book.end_date)
    else:
        month_query = ""

    if user_id is not None:
        user_query = " AND tu.id = " + str(user_id)
    else:
        user_query = ""

    raw_query = """
      SELECT
          te.id                        AS id
        , te.cost                      AS cost  
        , te.year                      AS year
        , te.status                    AS status
        , COALESCE(ts.name, ta.title)  AS site_name
        , ta.first_name                AS account_first_name
        , ta.last_name                 AS account_last_name
        , te.withdrawn_date            AS withdrawn_date
        , CASE WHEN te.approved_date IS NULL
            THEN FALSE 
            ELSE TRUE
          END AS approved
      FROM
        tms_earning AS te
      INNER JOIN tms_account AS ta ON te.account_id = ta.id
      LEFT JOIN tms_site AS ts ON ta.site_id = ts.id
      INNER JOIN tms_user AS tu ON te.earned_by_id = tu.id
        %s
      WHERE te.deleted_at IS NULL
        %s
        %s
        %s
      ORDER BY te.withdrawn_date ASC
    ;
    """ % (month_query, account_query, year_query, user_query)
    earnings = Earning.objects.raw(raw_query)
    ret = []
    summary = 0.0
    for earning in earnings:
        ret.append({
            "id": earning.id,
            "cost": earning.cost,
            "year": earning.year,
            "status": earning.status,
            "site_name": earning.site_name,
            "withdrawn_date": earning.withdrawn_date,
            "account_first_name": earning.account_first_name,
            "account_last_name": earning.account_last_name,
            "approved": earning.approved,
        })
        summary += earning.cost

    return ret, summary


def get_pending_earnings(team_id=None):
    if team_id is not None:
        team_query = "AND tu.team_id = %s" % (team_id, )
    else:
        team_query = ""

    raw_query = """
      SELECT
          te.id                        AS id
        , tu.first_name                AS member_first_name
        , tu.last_name                 AS member_last_name
        , COALESCE(ts.name, ta.title)  AS site_name
        , ta.first_name                AS account_first_name
        , ta.last_name                 AS account_last_name
        , tu.id                        AS user_id
        , te.cost                      AS cost
        , te.withdrawn_date            AS withdrawn_date
      FROM
        tms_earning AS te
      INNER JOIN tms_account AS ta ON te.account_id = ta.id
      LEFT JOIN tms_site AS ts ON ta.site_id = ts.id
      INNER JOIN tms_user AS tu ON te.earned_by_id = tu.id
      WHERE te.approved_by_id IS NULL
        AND te.approved_date IS NULL
        AND te.deleted_at IS NULL
        %s
      ORDER BY ta.id ASC, te.withdrawn_date ASC
    ; 
    """ % (team_query, )

    pending_earnings = Earning.objects.raw(raw_query)
    ret = []
    for earning in pending_earnings:
        ret.append({
            "id": earning.id,
            "member_first_name": earning.member_first_name,
            "member_last_name": earning.member_last_name,
            "site_name": earning.site_name,
            "account_first_name": earning.account_first_name,
            "account_last_name": earning.account_last_name,
            "cost": earning.cost,
            "withdrawn_date": earning.withdrawn_date,
        })

    return ret
