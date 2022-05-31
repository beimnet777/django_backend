from django.urls import path
from .views import login,Logout

urlpatterns = [ 
          path('login/',login.as_view()),
          path('logout/',Logout.as_view()),
]