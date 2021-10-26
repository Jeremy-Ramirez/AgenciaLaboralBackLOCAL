
from applications.Profesiones.serializers import ProfesionesSerializer
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [

path('profesiones/',views.ProfesionesApiView.as_view(),name="profesiones api")
  
    
]