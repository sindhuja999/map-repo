# todo/todo_api/views.py
import re
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from .models import Geolocation, CustomUser
from .serializers import GeolocationSerializer, UserSerializer


# class TodoListApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the todo items for given requested user
#         '''
#         todos = Geolocation.objects.all()
#         serializer = GeolocationSerializer(todos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Todo with given todo data
#         '''
#         # return Response(request.body)
#         body = json.loads(request.body)
#         data = {
#             'id': body.get('id'), 
#             'name': body.get('name'), 
#             'latitude': body.get('latitude'),
#             'longitude': body.get('longitude')
#         }
#         serializer = GeolocationSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserViewset(viewsets.ModelViewSet):
   permission_classes = (permissions.IsAuthenticated, )
   queryset = CustomUser.objects.all()
   serializer_class = UserSerializer

class TodoListApiView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer