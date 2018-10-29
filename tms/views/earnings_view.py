from rest_framework import viewsets
from tms.models import Earning
from tms.serializers import EarningSerializer


class EarningsView(viewsets.ViewSet):
    serializer_class = EarningSerializer

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
