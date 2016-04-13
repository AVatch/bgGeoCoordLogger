from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Coordinates
from .serializers import CoordinatesSerializer


class CoordinateLoggerAPIHandler(APIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format=None):
        """
        Log the coordinates and associate them wtih a user
        """
        
        # serializer = CoordinatesSerializer( data=request.data )
    
    
        coords = Coordinates.objects.create(
            altitude = request.data.get('location').get('coords').get('altitude'),
            longitude = request.data.get('location').get('coords').get('longitude'),
            latitude = request.data.get('location').get('coords').get('latitude'),
            altitudeAccuracy = request.data.get('location').get('coords').get('altitudeAccuracy'),
            accuracy = request.data.get('location').get('coords').get('accuracy'),
            
            is_moving = request.data.get('location').get('is_moving'),
            
            
            account = request.user
        )
        return Response( { 'id': coords.id }, status=status.HTTP_201_CREATED )
