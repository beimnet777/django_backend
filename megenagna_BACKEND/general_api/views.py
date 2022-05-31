from rest_framework import generics,viewsets
from django.contrib.auth.models import User

from general_api.pagination import customPageNumberPagination
from .models import EmployeeProfile, EmployerProfile, Job,Application
from .serializer import EmployeeSerializer,EmployerSerializer,JobSerializer,EmployeeUserSerializer,EmployerUserSerializer,ApplicationSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmployeeProfileView(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class EmployerProfileView(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated]

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
class EmployeeUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeUserSerializer
    
class EmployerUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployerUserSerializer
    
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
class JobLister(generics.ListAPIView):
    queryset = Job.objects.all()
    pagination_class = customPageNumberPagination
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    permission_classes = [IsAuthenticated]
