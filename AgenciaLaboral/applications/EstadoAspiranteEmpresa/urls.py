from applications.EstadoAspiranteEmpresa.serializers import EstadoAspiranteEmpresaSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('estadoaspiranteempresa/', views.EstadoAspiranteEmpresaApiView.as_view(), name='Estado Aspirante Empresa api'),
     path('estadoaspiranteempresa/<int:pk>', EstadoAspiranteEmpresaApiView.as_view()),
   
]