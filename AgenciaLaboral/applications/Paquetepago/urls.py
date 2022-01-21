from applications.Paquetepago.serializers import PaquetepagoSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('paquetePago/', views.PaquetepagoApiView.as_view(), name='Paquete de pago api'),
     path('paquetePago/<int:pk>', PaquetepagoApiView.as_view()),
   
]