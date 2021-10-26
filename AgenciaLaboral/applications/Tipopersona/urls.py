from applications.Tipopersona.serializers import TipopersonaSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('tipopersona/', views.TipopersonaApiView.as_view(), name='tipopersona api'),     
     path('tipopersona/<int:pk>', TipopersonaApiView.as_view()),
   
]
