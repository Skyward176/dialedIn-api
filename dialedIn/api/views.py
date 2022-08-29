from dialedIn.api.models import Extraction, Coffee
from rest_framework import viewsets
from rest_framework import permissions
from dialedIn.api.serializers import ExtractionSerializer, CoffeeSerializer
from rest_framework.response import Response
from rest_framework import views
from django.contrib.auth import login
from rest_framework import status


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