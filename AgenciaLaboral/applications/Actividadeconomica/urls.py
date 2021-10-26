from applications.Actividadeconomica.serializers import ActividadeconomicaSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('actividadeconomica/', views.ActividadeconomicaApiView.as_view(), name='Actividadeconomica api'),   
     path('actividadeconomica/<int:pk>', ActividadeconomicaApiView.as_view()),
]
