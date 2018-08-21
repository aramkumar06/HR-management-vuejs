from rest_framework import serializers

from tms.models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id'
            'name',
            'code'
        )
