from tms.models import Earning


def get_earnings(account_id=None, client_id=None, project_id=None, year=None, month=None, week=None):
    if project_id is not None:
        project_query = " AND tp.id = " + project_id
    else:
        project_query = ""

    if client_id is not None:
        client_query = " AND tc.id = " + client_id
    else:
        client_query = ""

    if account_id is not None:
        account_query = " AND ta.id = " + account_id
    else:
        account_query = ""

    if week is not None:
        week_query = " AND te.week_of_year = " + week
    else:
        week_query = ""

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
          , tc.first_name AS client_first_name
          , tc.last_name AS client_last_name
          , tp.title AS project_title 
        FROM
          tms_earning AS te
        INNER JOIN tms_project AS tp ON te.project_id = tp.id
        INNER JOIN tms_client AS tc ON tp.client_id = tc.id
        INNER JOIN tms_account AS ta ON tc.account_id = ta.id
        INNER JOIN tms_site AS ts ON ta.site_id = ts.id
        INNER JOIN tms_user AS tu ON tp.user_in_charge_id = tu.id
        %s
        WHERE te.deleted_at IS NULL
        %s
        %s
        %s
        %s
        %s
        ORDER BY te.week_of_year ASC
    ;
    """ % (month_query, project_query, client_query, account_query, week_query, year_query)
    earnings = Earning.objects.raw(raw_query)
    ret = []
    summary = 0.0
    for earning in earnings:
        ret.append({
            "id": earning.id,
            "cost": earning.cost,
            "year": earning.year,
            "week_of_year": earning.week_of_year,
            "status": earning.status,
            "site_name": earning.site_name,
            "account_first_name": earning.account_first_name,
            "account_last_name": earning.account_last_name,
            "client_first_name": earning.client_first_name,
            "client_last_name": earning.client_last_name,
            "project_title": earning.project_title
        })
        summary += earning.cost

    return ret, summary
