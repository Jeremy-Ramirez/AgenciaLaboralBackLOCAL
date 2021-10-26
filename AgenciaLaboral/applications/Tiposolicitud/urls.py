from applications.Tiposolicitud.serializers import TiposolicitudSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('tiposolicituds/', views.TiposolicitudApiView.as_view(), name='tiposolicitudes api'),     
     path('tiposolicituds/<int:pk>', TiposolicitudApiView.as_view()),
   
]
