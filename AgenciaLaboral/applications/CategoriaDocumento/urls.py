from applications.Genero.serializers import GeneroSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('categoriadocumento/', views.CategoriaDocumentoApiView.as_view(), name='categoria documento api'),
     path('categoriadocumento/<int:pk>', CategoriaDocumentoApiView.as_view()),
   
]