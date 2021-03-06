from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
	"""Serializes a name for APIView"""
	name = serializers.CharField(max_length=10)

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = models.User
		fields = ('id', 'email', 'first_name', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self,validated_data):
		"""create and return user"""
		user = models.User(
				email = validated_data['email'],
				first_name = validated_data['first_name'],
			)

		user.set_password(validated_data['password'])
		user.save()

		return user

class LocationSerializer(serializers.ModelSerializer):
	"""Serializer for Location items"""
	class Meta:
		model = models.Location
		fields = ('id', 'user_profile', 'gps_longitude', 'gps_latitude', 'created_on')
		extra_kwargs = {'user_profile': {'read_only': True}}