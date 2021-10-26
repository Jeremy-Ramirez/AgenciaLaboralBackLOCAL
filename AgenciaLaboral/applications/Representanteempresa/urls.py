from applications.Representanteempresa.serializers import RepresentanteEmpresaSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('representantes/', views.RepresentanteEmpresaApiView.as_view(), name='representantes api'),
     path('representantes/<int:pk>', views.RepresentanteEmpresaApiView.as_view()),

]