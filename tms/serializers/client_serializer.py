from rest_framework import serializers

from tms.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'skype',
            'phone_number',
            'url',
            'recital',
            'country',
            'account',
            'site'
        )
