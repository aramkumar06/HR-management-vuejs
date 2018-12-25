from rest_framework import viewsets
from tms.models import Site
from tms.serializers import SiteSerializer


class SitesView(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
