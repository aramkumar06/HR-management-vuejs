from django.core.exceptions import PermissionDenied

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from tms.services.rewards_service import *

class RewardsView(viewsets.GenericViewSet):
    def check_object_permissions(self, request, obj):
        pass

    def check_admin(self, request):
        delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
        if request.user.role_id != delegate_role_id:
            raise PermissionDenied()

    @action(detail=False, methods=['post'])
    def list_teams_reward(self, request):
        try:
            self.check_admin(request)

            ret = get_teams_rewards()
            response = Response({
                'success': True,
                'data': ret,
                'message': 'successfully fetched!',
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission',
            })

        return response

    @action(detail=False, methods=['post'])
    def team_last_reward(self, request):
        team_id = request.data.get('team_id', None)
        ret = get_current_team_reward(team_id)

        response = Response({
            'success': True,
            'data': ret,
            'message': 'successfully fetched!',
        })

        return response

    @action(detail=False, methods=['post'])
    def approve_team_reward(self, request):
        try:
            self.check_admin(request)

            team_id = request.data.get('team_id', None)
            if not team_id:
                raise Exception("team_id should be provided")

            awarded = award_bonus_team(team_id)
            if awarded:
                response = Response({
                    'success': True,
                    'message': 'awarded bonus to team'
                })
            else:
                response = Response({
                    'success': False,
                    'message': 'error occurs while awarding'
                })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })
        except Exception as e:
            response = Response({
                'success': False,
                'message': str(e)
            })

        return response
