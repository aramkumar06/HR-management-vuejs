from rest_framework import  serializers

from tms.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'start_date',
            'end_date',
            'status',
            'project_type',
            'price',
            'limit',
            'posted_datetime',
            'applied_datetime',
            'applied_proposals_count',
            'interview_count',
            'account',
            'client'
        )
