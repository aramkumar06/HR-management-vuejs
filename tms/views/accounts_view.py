from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from tms.models import Account
from tms.serializers import AccountSerializer


class AccountsView(viewsets.ViewSet):
    serializer_class = AccountSerializer
    authentication_classes = (SessionAuthentication, BaseAuthentication)

    def check_object_permissions(self, request, obj):
        if obj.user_id != request.user.id:
            raise PermissionDenied()

    def list(self, request):
        # TODO
        # for all params, should return all accounts when has permission
        # return only user accounts
        accounts = Account.objects.filter(user_id__exact=request.user.id)
        serializer = self.serializer_class(data=accounts, many=True)
        serializer.is_valid()
        if serializer.errors:
            response = Response({
                'success': False,
                'message': 'occurred an error!'
            })
        else:
            response = Response({
                'success': True,
                'accounts': serializer
            })

        return response

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            response = Response({
                'success': False,
                'message': 'occurred an error!'
            })
        else:
            account = serializer.validated_data['account']
            created = Account.objects.create(account)
            response = Response({
                'success': True,
                'id': created.id
            })

        return response

    def retrieve(self, request, pk=None):
        try:
            account = Account.objects.get(pk=pk)
            self.check_object_permissions(request, account)
            serializer = self.serializer_class(data=account)
            response = Response({
                'success': True,
                'account': serializer
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
        try:
            account = Account.objects.get(pk=pk)
            self.check_object_permissions(request, account)
            serializer = self.serializer_class(data=account)
            account.save(update_fields=serializer)
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


router = DefaultRouter()
router.register(r'accounts', AccountsView, 'accounts')
