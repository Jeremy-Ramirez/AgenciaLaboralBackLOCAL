from applications.DuracionPaquetes.serializers import DuracionPaquetesSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('duracionpaquetes/', views.DuracionPaquetesApiView.as_view(), name='Duracion Paquetes api'),
     path('duracionpaquetes/<int:pk>', DuracionPaquetesApiView.as_view()),
   
]