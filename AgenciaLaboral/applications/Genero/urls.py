from applications.Genero.serializers import GeneroSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('genero/', views.GeneroApiView.as_view(), name='generos api'),
   
]
