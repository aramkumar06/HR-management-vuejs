from rest_framework import serializers

from tms.models import Earning


class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = (
            'id',
            'cost',
            'year',
            'status',
            'withdrawn_date',
            'comments',
            'earned_by',
            'account',
            'approved_date',
            'approved_by',
            'finance_account',
        )
