from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import PermissionDenied
from tms.services.report_service import *


class ReportsView(viewsets.GenericViewSet):
    def check_object_permissions(self, request, obj):
        pass

    @action(detail=False, methods=['post'])
    def member(self, request):
        # TODO
        #  check permissions
        #
        year = request.data.get('year', None)
        month = request.data.get('month', None)
        team_id = request.user.team_id
        earnings_by_member, summary = report_member(team_id, year, month)
        response = Response({
            'success': True,
            'earnings_by_member': earnings_by_member,
            'summary': summary,
        })

        return response

    @action(detail=False, methods=['post'])
    def team(self, request):
        # TODO
        #  check permissions
        #
        year = request.data.get('year', None)
        month = request.data.get('month', None)
        earnings_by_team, summary = report_team(year, month)
        response = Response({
            'success': True,
            'earnings_by_team': earnings_by_team,
            'summary': summary,
        })

        return response
