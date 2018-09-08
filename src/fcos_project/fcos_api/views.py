from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

from rest_framework import viewsets


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
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
