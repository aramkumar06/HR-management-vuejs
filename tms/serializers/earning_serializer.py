from rest_framework import serializers

from tms.models import Earning


class EarningSerializer(serializers.HyperlinkedModelSerializer):
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
            'week_year',
            'updated_date',
            'status',
            'project',
            'earn_type'
        )
