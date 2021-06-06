from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import CoronaAPI
from .serializers import UserFetchCovDataSerializer

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

corapi = CoronaAPI()

def index(request):
    return HttpResponse("Hello, Aubergines")

class CovidFetchView(CreateAPIView):

    serializer_class = UserFetchCovDataSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post',]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        if data["country"] == "":
            ccode = request.user.country
        else:
            ccode = data["country"]
        tline = data["timeline"]
        [output, code] = corapi.getCovidData(ccode, tline)
        if (code == 200):
            return(Response(output, status.HTTP_200_OK))
        else:
            return(Response(output, status.HTTP_404_NOT_FOUND))