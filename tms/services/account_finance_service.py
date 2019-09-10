from tms.models import AccountFinance


def get_financial_accounts(financial_account_id=None):
    if financial_account_id is not None:
        financial_query = "AND tms_accountfinance.financial_account_id = %s" % (financial_account_id, )
    else:
        financial_query = ""

    raw_query = """
        SELECT
            tms_accountfinance.id                      AS id
          , tms_accountfinance.email_account_id        AS email_account_id
          , tms_accountfinance.financial_account_id    AS financial_account_id
          , email_account.email                        AS account_email
          , finance_account.first_name                 AS account_finance_first_name
          , finance_account.last_name                  AS account_finance_last_name
          , finance_account.title                      AS account_finance_site_name
          , owner.first_name                           AS owner_first_name
          , owner.last_name                            AS owner_last_name
        FROM
          tms_accountfinance
          INNER JOIN tms_account AS email_account ON tms_accountfinance.email_account_id = email_account.id
          INNER JOIN tms_account AS finance_account ON tms_accountfinance.financial_account_id = finance_account.id
          INNER JOIN tms_user AS owner ON email_account.user_id = owner.id
        WHERE
          tms_accountfinance.deleted_at IS NULL
          %s
        ORDER BY tms_accountfinance.financial_account_id ASC, tms_accountfinance.email_account_id ASC
    """ % (financial_query, )

    financial_accounts = AccountFinance.objects.raw(raw_query)

    ret = []
    for finance_account in financial_accounts:
        ret.append({
            'id': finance_account.id,
            'email_account_id': finance_account.email_account_id,
            'financial_account_id': finance_account.financial_account_id,
            'account_email': finance_account.account_email,
            'finance_first_name': finance_account.account_finance_first_name,
            'finance_last_name': finance_account.account_finance_last_name,
            'finance_site_name': finance_account.account_finance_site_name,
            'owner_first_name': finance_account.owner_first_name,
            'owner_last_name': finance_account.owner_last_name,
        })

    return ret
