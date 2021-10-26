from applications.Ciudad.serializers import CiudadSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('ciudades/', views.CiudadApiView.as_view(), name='ciudades api'),
     path('ciudades/<int:pk>', CiudadApiView.as_view()),
]
