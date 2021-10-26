from applications.Sector.serializers import SectorSerializer
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
  
     path('sectores/', views.SectorApiView.as_view(), name='sectores api'),     
     path('sectores/<int:pk>', SectorApiView.as_view()),
   
]