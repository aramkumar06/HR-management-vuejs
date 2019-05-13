from rest_framework import serializers

from tms.models import Earning


class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = (
            'id',
            'cost',
            'week_of_year',
            'year',
            'status',
            'project',
            'approved_date',
            'withdrawn_date',
            'approved_by'
        )
