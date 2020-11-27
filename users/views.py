from django.contrib.auth import authenticate, settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_200_OK
)
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer

import jwt

class UserViewSet(ModelViewSet):

    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class LoginView(APIView):
    def get(self, request):
        return Response({'detail': 'Only POST request allowed'}, status=HTTP_405_METHOD_NOT_ALLOWED)
  
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(status=HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        # add expiray FIXME
        if user is not None:
            encoded_jwt = jwt.encode(
                {'pk': user.pk}, settings.SECRET_KEY, algorithm='HS256'
            )
            return Response({'token': encoded_jwt, 'id': user.pk}, status=HTTP_200_OK)
        else:
            return Response(status=HTTP_401_UNAUTHORIZED)

