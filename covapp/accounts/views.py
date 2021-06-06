from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.parsers import JSONParser

from .serializers import UserCreateSerializer, UserTokenSerializer


class UserRegistrationView(CreateAPIView):

    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post',]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        response = {
            'success': 'True',
            'status code': status.HTTP_201_CREATED,
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
 
class CustomAuthToken(ObtainAuthToken):
    
    parser_classes = [JSONParser,]
    permission_classes = (AllowAny,)
    http_method_names = ['post',]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })