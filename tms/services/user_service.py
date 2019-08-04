import os

from tms.models import User


def get_delegation_members():
    role_delegate_id = os.getenv('ROLE_DELEGATE_ID')
    raw_query = """
        SELECT
            tu.id         AS id
          , tu.first_name AS first_name
          , tu.last_name  AS last_name
          , tu.name       AS name
          , tu.username   AS username
        FROM tms_user AS tu
        WHERE tu.deleted_at IS NULL
          AND tu.is_active IS TRUE
          AND tu.role_id <> %s
        ORDER BY tu.id
        ;
    """ % (role_delegate_id, )

    members = User.objects.raw(raw_query)
    ret = []
    for member in members:
        ret.append({
            "id": member.id,
            "first_name": member.first_name,
            "last_name": member.last_name,
            "name": member.name,
            "username": member.username,
        })

    return ret
