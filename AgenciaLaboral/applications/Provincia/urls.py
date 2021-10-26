from applications.Provincia.serializers import ProvinciaSerializer
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
  
     path('provincias/', views.ProvinciaApiView.as_view(), name='provincias api'),
     path('provincias/<int:pk>', ProvinciaApiView.as_view()),
]