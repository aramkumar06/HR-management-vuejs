from rest_framework import serializers

from tms.models import Site


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = (
            'id',
            'name',
            'url',
            'description'
        )
