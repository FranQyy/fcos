from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models

from rest_framework import viewsets

from . import permissions

from rest_framework import filters

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.permissions import IsAuthenticated

class HelloApiView(APIView):

	serializer_class = serializers.HelloSerializer

	def get(self,request,format=None):
		an_apiview = [
			'Et harum quidem rerum',
			'facilis est et expedita distinctio',
			'Nam libero tempore, cum soluta nobis est eligendi',
			'optio cumque nihil impedit quo minus id quod maxime placeat facere possimus',
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})

	def post(self, request):
		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		"""updates an object"""

		return Response({'method': 'put'})

	def patch(self, request, pk=None):
		"""only updates fields provided in the request"""

		return Response({'method': 'patch'})

	def delete(self, request, pk=None):
		"""deletes an object"""

		return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""return hello"""
		a_viewset = [
			'1Et harum quidem rerum',
			'2facilis est et expedita distinctio',
			'3Nam libero tempore, cum soluta nobis est eligendi',
			'4optio cumque nihil impedit quo minus id quod maxime placeat facere possimus',
		]

		return Response({'message': 'Hello!', 'a_viewset': a_viewset})

	def create(self, request):
		"""create a new hello message"""
		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def retrieve(self,request,pk=None):
		
		return Response({'http_method': 'GET'})

	def update(self, request, pk=None):
		
		return Response({'http_method': 'PUT'})

	def partial_update(self, request, pk=None):

		return Response({'http_method': 'PATCH'})		

	def destroy(self, request, pk=None):

		return Response({'http_method': 'DELETE'})

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.UserSerializer
	queryset = models.User.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('first_name', 'email',)

class LoginViewSet(viewsets.ViewSet):
	serializer_class = AuthTokenSerializer
	def create(self, request):
		return ObtainAuthToken().post(request)

class LocationViewSet(viewsets.ModelViewSet):
	authentication_classes = (TokenAuthentication,)
	serializer_class = serializers.LocationSerializer
	queryset = models.Location.objects.all()
	permission_classes = (permissions.PostOwnLocation, IsAuthenticated)

	def perform_create(self, serializer):
		"""Sets the user profile to the logged in user"""
		serializer.save(user_profile=self.request.user)
