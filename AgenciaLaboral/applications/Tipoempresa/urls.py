from applications.Tipoempresa.serializers import TipoempresaSerializer
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
  
     path('tipoempresas/', views.TipoempresaApiView.as_view(), name='tipoempresas api'),     
     path('tipoempresas/<int:pk>', TipoempresaApiView.as_view()),
   
]