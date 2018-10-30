from rest_framework import serializers

from tms.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'email_password',
            'skype',
            'skype_password',
            'status',
            'phone_number',
            'created_date',
            'suspended_date',
            'registered_date',
            'recital',
            'title',
            'overview',
            'country',
            'user',
            'site'
        )
