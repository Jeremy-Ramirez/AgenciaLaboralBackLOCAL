from applications.Estado.serializers import EstadoSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('estados/', views.EstadoApiView.as_view(), name='estados api'),
     path('estados/<int:pk>', EstadoApiView.as_view()),
   
]
