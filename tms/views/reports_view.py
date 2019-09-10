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
            'message': 'successfully fetched!',
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
            'message': 'successfully fetched!',
        })

        return response

    @action(detail=False, methods=['post'])
    def delegate(self, request):
        # TODO
        #  check permissions
        #
        try:
            delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
            if request.user.role_id != delegate_role_id:
                raise PermissionDenied

            year = request.data.get('year', None)
            month = request.data.get('month', None)
            earnings_by_delegate, summary = report_delegation(year, month)
            response = Response({
                'success': True,
                'earnings_by_delegate': earnings_by_delegate,
                'summary': summary,
                'message': 'successfully fetched!'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission',
            })

        return response

    @action(detail=False, methods=['post'])
    def total_monthly_per_member(self, request):
        # TODO
        #  check permissions
        #
        try:
            year = request.data.get('year', None)
            earnings_total, summary_year = report_monthly_summary_individual(year, request.user.id)
            response = Response({
                'success': True,
                'earnings': earnings_total,
                'summary': summary_year,
                'message': 'successfully fetched!',
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission',
            })

        return response

    @action(detail=False, methods=['post'])
    def total_summary_by_member(self, request):
        # TODO
        #  check permissions
        #
        try:
            delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
            if request.user.role_id != delegate_role_id:
                raise PermissionDenied

            year = request.data.get('year', None)
            earnings, summary = report_total_summary_by_member(year)
            response = Response({
                'success': True,
                'earnings': earnings,
                'summary': summary,
                'message': 'successfully fetched!',
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission',
            })

        return response
