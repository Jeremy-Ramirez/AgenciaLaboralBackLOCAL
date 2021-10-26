from applications.Solicitud.serializers import SolicitudSerializer
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
  
     path('solicitudes/', views.SolicitudApiView.as_view(), name='solicitudes api'),     
     path('solicitudes/<int:pk>', SolicitudApiView.as_view()),
   
]