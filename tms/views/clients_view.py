from rest_framework import viewsets
from tms.models import Client
from tms.serializers import ClientSerializer


class ClientsView(viewsets.ViewSet):
    serializer_class = ClientSerializer

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
