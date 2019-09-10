import os

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from tms.serializers import UserSerializer

from tms.models import Book

class CustomAuthToken(ObtainAuthToken):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            response = Response({
                'success': False
            })
        else:
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            book_dates = {}
            rows = Book.objects.all().order_by('year').order_by('month')
            for row in rows:
                if row.year not in book_dates.keys():
                    book_dates[row.year] = [row.month]
                else:
                    book_dates[row.year].append(row.month)

                if row.status == Book.STATUS_ACTIVE:
                    active_year = row.year
                    active_month = row.month

            team_id = user.team.id if user.team else None
            is_boss = user.role_id == int(os.getenv('ROLE_DELEGATE_ID'))

            response = Response({
                'success': True,
                'token': token.key,
                'id': user.id,
                'team_id': team_id,
                'role_id': user.role.id,
                'role_name': user.role.name,
                'book_dates': book_dates,
                'active_year': active_year,
                'active_month': active_month,
                'is_boss': is_boss,
            })

        return response
