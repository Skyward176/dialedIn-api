from dialedIn.api.models import Extraction, Coffee
from rest_framework import viewsets
from rest_framework import permissions
from dialedIn.api.serializers import ExtractionSerializer, CoffeeSerializer, LoginSerializer
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
class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)