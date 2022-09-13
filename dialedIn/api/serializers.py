from dialedIn.api.models import Extraction, Coffee
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class ExtractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extraction
        fields = ['user_id', 'coffee_id', 'timestamp', 'extraction_length','mass_in','mass_out','notes']


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ['id','coffee_name', 'roaster_name', 'roast_level']
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
