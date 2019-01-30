from rest_framework import serializers

from tms.models import Earning


class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = (
            'id',
            'cost',
            'start_week_date',
            'end_week_date',
            'week_of_year',
            'month_of_year',
            'year',
            'confirmed',
            'project',
            'approved_date',
            'withdrawn_date',
            'approved_by'
        )
