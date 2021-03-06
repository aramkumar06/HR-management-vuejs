import os
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import PermissionDenied
from tms.serializers import AccountSerializer
from tms.services.account_service import *


class AccountsView(viewsets.ViewSet):
    serializer_class = AccountSerializer

    def check_object_permissions(self, request, obj):
        if obj.user_id != request.user.id:
            raise PermissionDenied()

    def list(self, request):
        # TODO
        # v2
        #   role based query
        #
        delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
        if request.user.role_id == delegate_role_id:
            ret = get_delegation_accounts()
        else:
            ret = get_user_accounts(request.user.id)

        response = Response({
            'success': True,
            'accounts': ret,
            'message': 'successfully fetched!'
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
                'account': serializer.data,
                'message': 'successfully fetched!'
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
                'message': 'successfully removed',
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

    @action(detail=False, methods=['post'])
    def with_common(self, request):
        ret = get_self_and_common_accounts(request.user.id)
        response = Response({
            'success': True,
            'accounts': ret,
            'message': 'successfully fetched!'
        })

        return response

    @action(detail=False, methods=['post'])
    def payments(self, request):
        try:
            delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
            if request.user.role_id != delegate_role_id:
                raise PermissionDenied

            ret = get_payment_accounts()
            response = Response({
                'success': True,
                'accounts': ret,
                'message': 'successfully fetched!'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permissions'
            })
        except Exception as e:
            response = Response({
                'success': False,
                'message': str(e)
            })

        return response

    @action(detail=False, methods=['post'])
    def freelancing_accounts(self, request):
        try:
            delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
            if request.user.role_id != delegate_role_id:
                raise PermissionDenied

            ret = get_freelancing_accounts()
            response = Response({
                'success': True,
                'accounts': ret,
                'message': 'successfully fetched!'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permissions'
            })
        except Exception as e:
            response = Response({
                'success': False,
                'message': str(e)
            })

        return response
