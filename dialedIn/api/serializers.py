from dialedIn.api.models import Extraction, Coffee
from rest_framework import serializers
from django.contrib.auth import authenticate

class ExtractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extraction
        fields = ['user_id', 'coffee_id', 'timestamp', 'extraction_length','mass_in','mass_out','notes']


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ['id','coffee_name', 'roaster_name', 'roast_level']
