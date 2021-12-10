from applications.EstadoAspirantes.serializers import EstadoAspirantesSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('estadoaspirantes/', views.EstadoAspirantesApiView.as_view(), name='Estado Aspirantes api'),
     path('estadoaspirantes/<int:pk>', EstadoAspirantesApiView.as_view()),
   
]