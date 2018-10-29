from rest_framework import viewsets
from tms.models import Country
from tms.serializers import CountrySerializer


class CountriesView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
