from rest_framework import serializers

from tms.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'description',
        )
