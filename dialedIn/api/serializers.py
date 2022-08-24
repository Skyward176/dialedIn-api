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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )

    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(request = self.context.get('request'), username = username, password = password)

            if not user:
                msg = 'Username or Password Incorrect'
                raise serializers.ValidationError(msg, code = 'authorization')
        else:
            msg = 'Please input both username and password'
            raise serializers.ValidationError(msg, code = 'authorization')
        
        attrs['user'] = user
        return attrs