from rest_framework import generics,viewsets
from django.contrib.auth.models import User
from .models import EmployeeProfile, EmployerProfile, Job
from .serializer import EmployeeSerializer,EmployerSerializer,JobSerializer,EmployeeUserSerializer,EmployerUserSerializer

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class EmployeeProfileView(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeSerializer

class EmployerProfileView(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
class EmployeeUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeUserSerializer
class EmployerUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployerUserSerializer
class JobLister(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job_name']
