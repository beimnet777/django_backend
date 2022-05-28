from django.urls import path,include
from .views import EmployeeProfileView,EmployerProfileView,JobViewSet,EmployeeUserViewSet,EmployerUserViewSet,JobLister
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('jobs',JobViewSet,basename='job')
router.register('employer',EmployerProfileView,basename='employer')
router.register('employee',EmployeeProfileView,basename='employee')
router.register('EmployeeUser',EmployerUserViewSet,basename='EmplyeeUser')
router.register('EmployerUser',EmployerUserViewSet,basename='EmployerUser')

urlpatterns = [ 
          path('api/v1/model/',include(router.urls)),
          path('api/v1/model/limited/',JobLister.as_view())
]
