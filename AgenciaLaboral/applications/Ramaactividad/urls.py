from applications.Ramaactividad.serializers import RamaactividadSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('ramaactividad/', views.RamaactividadApiView.as_view(), name='Ramaactividades api'),
     path('ramaactividad/<int:pk>', RamaactividadApiView.as_view()),
   
]
