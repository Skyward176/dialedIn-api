from rest_framework.decorators import permission_classes
from dialedIn.api.models import Extraction, Coffee
from rest_framework import viewsets
from rest_framework import permissions
from dialedIn.api.serializers import ExtractionSerializer, CoffeeSerializer, UserRegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import views
from django.contrib.auth import login
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
class ExtractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Extraction.objects.all()
    serializer_class = ExtractionSerializer


class CoffeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

class UserRegistrationView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserRegisterSerializer(data=data)

        if serializer.is_valid():
            user = User.objects.create_user(serializer.data.get('username'),
                                            serializer.data.get('email'),
                                            serializer.data.get('password'))

        return JsonResponse(serializer.data)
