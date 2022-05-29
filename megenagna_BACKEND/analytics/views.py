from general_api.models import Application
from rest_framework.decorators import api_view

from .models import Analytics
from rest_framework import status
from rest_framework.response import Response
from django.core import serializers


@api_view(['GET'])
def get_analytics(request,id):
  age_18_29= Application.objects.filter(age__range=(18, 29),job=id ).count()
  age_30_50= Application.objects.filter(age__range=(30, 50) ,job=id ).count()
  age_51= Application.objects.filter(age__range=(50, 100),job=id  ).count()

  dict={
    "age_18_29":age_18_29,
    "age_30_50":age_30_50,
    "age_51":age_51
  }


  
  analytic=Analytics(age_18_29=age_18_29,age_30_50=age_30_50,age_51=age_51)
  data = serializers.serialize("json", [analytic])
  
  
  return Response(data,status=status.HTTP_200_OK)



# Create your views here.
