from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from tms.models import Account
from tms.serializers import AccountSerializer


class AccountsView(viewsets.ViewSet):
    serializer_class = AccountSerializer

    def check_object_permissions(self, request, obj):
        if obj.user_id != request.user.id:
            raise PermissionDenied()

    def list(self, request):

        # TODO
        #   if user id is specified, return only user related accounts and share accounts like freelancer
        # v2
        #   role based query
        #
        raw_query = """  
          SELECT
                ta.id           AS id
              , ta.first_name   AS account_first_name
              , ta.last_name    AS account_last_name
              , ta.status       AS account_status
              , ta.email        AS account_email
              , tc.name         AS country_name
              , ts.name         AS site_name
          FROM
            tms_account AS ta
          INNER JOIN tms_site AS ts ON ta.site_id = ts.id
          INNER JOIN tms_country AS tc ON ta.country_id = tc.id
          WHERE ta.user_id = {user_id} OR ta.user_id IS NULL;
        """.format(
            user_id=request.user.id
        )
        accounts = Account.objects.raw(raw_query)
        ret = []
        for account in accounts:
            ret.append({
                "account_id": account.id,
                "account_first_name": account.account_first_name,
                "account_last_name": account.account_last_name,
                "account_status": account.account_status,
                "account_email": account.account_email,
                "country_name": account.country_name,
                "site_name": account.site_name,
            })
        response = Response({
            'success': True,
            'accounts': ret
        })

        return response

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            response = Response({
                'success': False,
                'message': serializer.errors
            })
        else:
            serializer.save()
            response = Response({
                'success': True,
                'message': 'successfully created!'
            })

        return response

    def retrieve(self, request, pk=None):
        try:
            account = Account.objects.get(pk=pk)
            serializer = self.serializer_class(account)
            response = Response({
                'success': True,
                'account': serializer.data
            })
        except Account.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a account'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    def update(self, request, pk=None):
        #
        # TODO
        # should check permission
        # for shared accounts, general user couldn't update account detail
        #
        try:
            account = Account.objects.get(pk=pk)
            self.check_object_permissions(request, account)
            serializer = self.serializer_class(data=request.data, instance=account)
            serializer.is_valid(raise_exception=True)
            if serializer.errors:
                response = Response({
                    'success': False,
                    'message': serializer.errors
                })
            else:
                serializer.save()
                response = Response({
                    'success': True,
                    'message': 'successfully updated!'
                })
        except Account.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a account'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        try:
            account = Account.objects.get(pk=pk)
            self.check_object_permissions(request, account)
            account.delete()
            response = Response({
                'success': True,
                'id': account.id
            })
        except Account.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a account'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response
