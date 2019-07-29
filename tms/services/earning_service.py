from tms.models import Earning


def get_earnings(account_id=None, year=None, month=None, user_id=None):
    if account_id is not None:
        account_query = " AND ta.id = " + account_id
    else:
        account_query = ""

    if month is not None:
        month_query = """
        INNER JOIN LATERAL (
            SELECT *
            FROM tms_book AS tb
            WHERE te.year = tb.year 
                AND te.week_of_year = ANY(tb.weeks)
                AND tb.month = %s
            LIMIT 1
        ) x ON TRUE
        """ % (month,)
    else:
        month_query = ""

    if year is not None:
        year_query = " AND te.year = " + year
    else:
        year_query = ""

    if user_id is not None:
        user_query = " AND tu.id = " + str(user_id)
    else:
        user_query = ""

    raw_query = """
        SELECT
            te.id AS id
          , te.cost AS cost  
          , te.year AS year
          , te.week_of_year AS week_of_year
          , te.status AS status
          , ts.name AS site_name
          , ta.first_name AS account_first_name
          , ta.last_name AS account_last_name 
        FROM
          tms_earning AS te
        INNER JOIN tms_account AS ta ON te.account_id = ta.id
        INNER JOIN tms_site AS ts ON ta.site_id = ts.id
        INNER JOIN tms_user AS tu ON te.earned_by_id = tu.id
        %s
        WHERE te.deleted_at IS NULL
        %s
        %s
        %s
        ORDER BY te.week_of_year ASC
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
            "account_first_name": earning.account_first_name,
            "account_last_name": earning.account_last_name,
        })
        summary += earning.cost

    return ret, summary
