from applications.Sugerencia.serializers import SugerenciaSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('sugerenciasEmpresa/', views.SugerenciaEmpresaApiView.as_view(), name='Sugerencias Empresa api'),
     path('sugerenciasEmpresa/<int:pk>', views.SugerenciaEmpresaApiView.as_view()),
   
]