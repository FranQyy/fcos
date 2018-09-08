from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

	def get(self,request,format=None):
		an_apiview = [
			'Et harum quidem rerum',
			'facilis est et expedita distinctio',
			'Nam libero tempore, cum soluta nobis est eligendi',
			'optio cumque nihil impedit quo minus id quod maxime placeat facere possimus',
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})