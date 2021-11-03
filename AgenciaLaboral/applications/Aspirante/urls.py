from applications.Aspirante.serializers import AspiranteSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('aspirantes/', views.AspiranteApiView.as_view(), name='aspirantes api'),
     path('aspirantes/<int:pk>', views.AspiranteApiView.as_view()),
   
]