from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .utils import CoronaAPI
from .serializers import UserFetchCovDataSerializer
from accounts.country import all_country_code_dict

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse

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
        valid_data = serializer.validated_data
        
        if "country" not in valid_data.keys():
            ccode = request.user.get_country_display()
        else:
            ccode = valid_data["country"]

        if "timeline" not in valid_data.keys():
            tline = datetime.now()
        else:
            tline = valid_data["timeline"]
        
        try:
            [output, code] = corapi.getCovidData(ccode, tline)
        except:
            return (Response({"message": "The request timed out"}, status.HTTP_408_REQUEST_TIMEOUT))
        if (code == 200):
            return (Response(output, status.HTTP_200_OK))
        else:
            return (Response(output, status.HTTP_400_BAD_REQUEST))