from tms.models import Account


def get_user_accounts(user_id=None):
    if user_id is None:
        return []

    raw_query = """
      SELECT
            ta.id                           AS id
          , ta.first_name                   AS account_first_name
          , ta.last_name                    AS account_last_name
          , ta.status                       AS account_status
          , ta.email                        AS account_email
          , tc.name                         AS country_name
          , COALESCE(ts.name, ta.title)     AS site_name
      FROM
        tms_account AS ta
      LEFT JOIN tms_site AS ts ON ta.site_id = ts.id
      INNER JOIN tms_country AS tc ON ta.country_id = tc.id
      WHERE ta.user_id = %s
        AND ta.suspended_date IS NULL
    ;""" % (user_id, )

    accounts = Account.objects.raw(raw_query)
    ret = []
    for account in accounts:
        ret.append({
            "id": account.id,
            "account_first_name": account.account_first_name,
            "account_last_name": account.account_last_name,
            "account_status": account.account_status,
            "account_email": account.account_email,
            "country_name": account.country_name,
            "site_name": account.site_name,
        })

    return ret


def get_delegation_accounts():
    raw_query = """
      SELECT
            ta.id                           AS id
          , ta.first_name                   AS account_first_name
          , ta.last_name                    AS account_last_name
          , ta.status                       AS account_status
          , ta.email                        AS account_email
          , tc.name                         AS country_name
          , COALESCE(ts.name, ta.title)     AS site_name
      FROM
        tms_account AS ta
      LEFT JOIN tms_site AS ts ON ta.site_id = ts.id
      INNER JOIN tms_country AS tc ON ta.country_id = tc.id
      WHERE ta.suspended_date IS NULL
      ORDER BY ts.id ASC NULLS FIRST
    ;"""

    accounts = Account.objects.raw(raw_query)
    ret = []
    for account in accounts:
        ret.append({
            "id": account.id,
            "account_first_name": account.account_first_name,
            "account_last_name": account.account_last_name,
            "account_status": account.account_status,
            "account_email": account.account_email,
            "country_name": account.country_name,
            "site_name": account.site_name,
        })

    return ret


def get_self_and_common_accounts(user_id=None):
    if user_id is None:
        return []

    raw_query = """
      SELECT
            ta.id                           AS id
          , ta.first_name                   AS account_first_name
          , ta.last_name                    AS account_last_name
          , ta.status                       AS account_status
          , ta.email                        AS account_email
          , tc.name                         AS country_name
          , COALESCE(ts.name, ta.title)     AS site_name
          , ta.is_payment_account AS is_payment_account
      FROM
        tms_account AS ta
      LEFT JOIN tms_site AS ts ON ta.site_id = ts.id
      INNER JOIN tms_country AS tc ON ta.country_id = tc.id
      WHERE (ta.user_id = %s
        AND ta.suspended_date IS NULL)
        OR ta.user_id IS NULL;
    """ % (user_id, )

    accounts = Account.objects.raw(raw_query)
    ret = []
    for account in accounts:
        ret.append({
            "id": account.id,
            "account_first_name": account.account_first_name,
            "account_last_name": account.account_last_name,
            "account_status": account.account_status,
            "account_email": account.account_email,
            "country_name": account.country_name,
            "site_name": account.site_name,
            "is_payment_account": account.is_payment_account,
        })

    return ret

def get_payment_accounts():
    raw_query = """
      SELECT
            ta.id                           AS id
          , ta.first_name                   AS account_first_name
          , ta.last_name                    AS account_last_name
          , ta.status                       AS account_status
          , ta.email                        AS account_email
          , COALESCE(ts.name, ta.title)     AS site_name
      FROM
        tms_account AS ta
      LEFT JOIN tms_site AS ts ON ta.site_id = ts.id
      WHERE ta.is_payment_account IS TRUE
        AND ta.deleted_at IS NULL
      ORDER BY site_name ASC
    ;"""

    accounts = Account.objects.raw(raw_query)
    ret = []
    for account in accounts:
        ret.append({
            "id": account.id,
            "account_first_name": account.account_first_name,
            "account_last_name": account.account_last_name,
            "account_status": account.account_status,
            "account_email": account.account_email,
            "site_name": account.site_name,
        })

    return ret

def get_freelancing_accounts():
    raw_query = """
          SELECT
                ta.id                           AS id
              , ta.first_name                   AS account_first_name
              , ta.last_name                    AS account_last_name
              , ta.status                       AS account_status
              , ta.email                        AS account_email
              , COALESCE(ts.name, ta.title)     AS site_name
          FROM
            tms_account AS ta
          LEFT JOIN tms_site AS ts ON ta.site_id = ts.id
          WHERE ta.is_payment_account IS FALSE
            AND ta.deleted_at IS NULL
            AND ta.suspended_date IS NULL
          ORDER BY site_name ASC
        ;"""

    accounts = Account.objects.raw(raw_query)
    ret = []
    for account in accounts:
        ret.append({
            "id": account.id,
            "account_first_name": account.account_first_name,
            "account_last_name": account.account_last_name,
            "account_status": account.account_status,
            "account_email": account.account_email,
            "site_name": account.site_name,
        })

    return ret
