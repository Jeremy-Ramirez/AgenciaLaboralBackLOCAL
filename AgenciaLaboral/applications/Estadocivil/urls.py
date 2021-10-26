from applications.Estadocivil.serializers import EstadocivilSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('estadocivils/', views.EstadocivilApiView.as_view(), name='Estadocivils api'),
     path('estadocivils/<int:pk>', EstadocivilApiView.as_view()),
   
]
