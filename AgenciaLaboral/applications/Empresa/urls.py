from applications.Empresa.serializers import EmpresaSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('empresas/', views.EmpresaApiView.as_view(), name='empresas api'),
     path('empresas/<int:pk>', EmpresaApiView.as_view()),
     path('loginempresa/', LoginView.as_view()),
     path('userempresa/', EmpresaView.as_view()),
     path('logoutempresa/', LogoutView.as_view())
]
