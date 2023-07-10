from rest_framework import serializers
from .models import Booking
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields ='__all__'
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']