from applications.Aspirantessolicitados.serializers import AspirantessolicitadosSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('aspirantessolicitados/', views.AspirantessolicitadosApiView.as_view(), name='aspirantessolicitados api'),
     path('aspirantessolicitados/<int:pk>', AspirantessolicitadosApiView.as_view()),
   
]
