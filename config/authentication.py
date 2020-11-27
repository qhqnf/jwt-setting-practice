import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication, exceptions

# with 'WSGIPathAuthorization On' if you are with server
# because aws automatically remove header

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token is None:
                raise exceptions.AuthenticationFailed('You should submit token')
            prefix, jwt_token = token.split(' ')
            decode = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            pk = decode.get('pk')
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not exist.')
        except jwt.exceptions.DecodeError: 
            raise exceptions.AuthenticationFailed('Invalid token')
        
        return (user, None)