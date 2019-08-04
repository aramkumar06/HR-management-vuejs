from rest_framework import viewsets
from rest_framework.response import Response

from tms.services.user_service import *


class UsersView(viewsets.ViewSet):
    def list(self, request):
        users = get_delegation_members()

        response = Response({
            'success': True,
            'users': users,
        })

        return response
