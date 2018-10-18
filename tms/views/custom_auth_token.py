from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from tms.serializers import UserSerializer


class CustomAuthToken(ObtainAuthToken):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            return Response({
            'success' : 0
            })
        else:            
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'success': 1,
                'token': token.key,
                'id': user.id
            })
