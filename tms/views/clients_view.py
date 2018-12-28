from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from tms.models import Client
from tms.serializers import ClientSerializer


class ClientsView(viewsets.ViewSet):
    serializer_class = ClientSerializer

    def check_object_permissions(self, request, obj):
        if obj.user_id != request.user.id:
            raise PermissionDenied()

    def list(self, request):
        raw_query = """
            SELECT
              , tc.id               AS id
              , tc.first_name       AS client_first_name
              , tc.last_name        AS client_last_name
              , tc.registered_date  AS client_registered_date
              , ta.first_name       AS account_first_name
              , ta.last_name        AS account_last_name
              , tc1.name            AS country_name
              , ts.name             AS site_name
            FROM
              tms_client AS tc
            INNER JOIN tms_account AS ta ON tc.account_id = ta.id;
            INNER JOIN tms_user AS tu ON ta.user_id = tu.id
            INNER JOIN tms_site AS ts ON tc.site_id = ts.id
            INNER JOIN tms_country AS tc1 ON tc.country_id = tc1.id
            WHERE tu.id = {user_id}
            {account_query};
        """.format(
            user_id=request.user.id
        )
        account_id = request.GET.get('account_id', None)
        if account_id is not None:
            account_query = "WHERE ta.id = " + account_id
            raw_query.format(account_query=account_query)
        else:
            raw_query.format(account_query="")

        clients = Client.objects.raw(raw_query)
        ret = []
        for client in clients:
            ret.append({
                "client_id": client.id,
                "client_first_name": client.client_first_name,
                "client_last_name": client.client_last_name,
                "client_registered_date": client.client_registered_date,
                "account_first_name": client.account_first_name,
                "account_last_name": client.account_last_name,
                "country_name": client.country_name,
                "site_name": client.site_name,
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
        pass

    def retrieve(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
            serializer = self.serializer_class(client)
            response = Response({
                'success': True,
                'client': serializer.data
            })
        except Client.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a client'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    def update(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
            self.check_object_permissions(request, client)
            serializer = self.serializer_class(data=request.data, instance=client)
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
        except Client.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a client'
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
            client = Client.objects.get(pk=pk)
            self.check_object_permissions(request, client)
            client.delete()
            response = Response({
                'success': True,
                'id': client.id
            })
        except Client.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a client'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response
