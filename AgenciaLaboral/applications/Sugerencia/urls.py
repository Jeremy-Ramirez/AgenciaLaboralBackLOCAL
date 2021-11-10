from applications.Sugerencia.serializers import SugerenciaSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('sugerencias/', views.SugerenciaApiView.as_view(), name='Sugerencias api'),
     path('sugerencias/<int:pk>', views.SugerenciaApiView.as_view()),
   
]