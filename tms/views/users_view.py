from django.core.exceptions import PermissionDenied

from rest_framework import viewsets
from rest_framework.response import Response

from tms.models import User
from tms.services.user_service import *


class UsersView(viewsets.ViewSet):
    def list(self, request):
        users = get_delegation_members()

        response = Response({
            'success': True,
            'users': users,
        })

        return response

    def update(self, request, pk):
        # TODO
        # permission check
        try:
            if int(request.user.id) != int(pk):
                raise PermissionDenied

            user = User.objects.get(pk=pk)
            password = request.data.get('password', None)
            password_confirmation = request.data.get('password_confirmation', None)

            if password is None or password_confirmation is None:
                raise Exception('password does not match')

            if password != password_confirmation:
                raise Exception('password does not match')

            user.set_password(password)
            user.save()

            response = Response({
                'success': True,
                'message': 'successfully updated'
            })
        except User.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a user'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })
        except Exception as e:
            print(e)
            response = Response({
                'success': False,
                'message': 'Error occurs while saving'
            })

        return response
