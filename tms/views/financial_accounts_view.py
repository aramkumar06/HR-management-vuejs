import os
import datetime

from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied

from tms.services.account_finance_service import *

class FinancialAccountsView(viewsets.ViewSet):
    def check_object_permissions(self, request):
        delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
        if request.user.role_id != delegate_role_id:
            raise PermissionDenied()

    def list(self, request):
        try:
            self.check_object_permissions(request)

            financial_account_id = request.GET.get('financial_account_id', None)
            ret = get_financial_accounts(financial_account_id)

            response = Response({
                'success': True,
                'accounts': ret
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    def retrieve(self):
        pass

    def create(self, request):
        try:
            self.check_object_permissions(request)

            account_finance_id = request.data.get('account_finance_id', None)
            account_email_id = request.data.get('account_email_id', None)
            if account_email_id is None or account_finance_id is None:
                raise Exception("not enough parameters are provided")

            # check whether already exists mapping
            mappings = AccountFinance.objects.filter(financial_account_id=account_finance_id, email_account_id=account_email_id, deleted_at__isnull=True).all()
            if len(mappings) > 0:
                raise Exception("already exists")

            account_finance = AccountFinance(financial_account_id=account_finance_id, email_account_id=account_email_id)
            account_finance.save()

            response = Response({
                'success': True,
                'message': 'successfully created'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })
        except Exception as e:
            response = Response({
                'success': False,
                'message': str(e)
            })

        return response

    def update(self):
        pass

    def destroy(self, request, pk=None):
        try:
            self.check_object_permissions(request)
            account_finance = AccountFinance.objects.get(pk=pk)
            account_finance.deleted_at = datetime.datetime.utcnow()
            account_finance.save()

            response = Response({
                'success': True,
                'message': 'account finance successfully removed'
            })
        except AccountFinance.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'account finance doesn\'t exist'
            })
        except AccountFinance.MultipleObjectsReturned:
            response = Response({
                'success': False,
                'message': 'too many account finance found'
            })

        return response
