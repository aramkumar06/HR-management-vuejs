from rest_framework import serializers

from tms.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'birthday',
            'address',
            'contact_number',
            'role',
            'team'
        )
