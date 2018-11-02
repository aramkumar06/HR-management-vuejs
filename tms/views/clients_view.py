from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from tms.models import Client
from tms.serializers import ClientSerializer


class ClientsView(viewsets.ViewSet):
    serializer_class = ClientSerializer

    def check_object_permissions(self, request, obj):
        if obj.account.user_id != request.user.id:
            raise PermissionDenied()

    def list(self, request):
        clients = Client.objects.all()
        serializer = self.serializer_class(clients, many=True)
        response = Response({
            'success': True,
            'accounts': serializer.data
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
            client = serializer.validated_data['client']
            created = Client.objects.create(client)
            response = Response({
                'success': True,
                'id': created.id
            })

        return response
        pass

    def retrieve(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
            serializer = self.serializer_class(data=client)
            response = Response({
                'success': True,
                'account': serializer
            })
        except Client.DoesNotExist:
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
            client = Client.objects.get(pk=pk)
            self.check_object_permissions(request, client)
            serializer = self.serializer_class(data=client)
            client.save(update_fields=serializer)
            response = Response({
                'success': True,
                'id': client.id
            })
        except Client.DoesNotExist:
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
                'message': 'no such a account'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response
