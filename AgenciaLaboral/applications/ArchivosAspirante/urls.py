from applications.ArchivosAspirante.serializers import ArchivosAspirantesSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('archivosaspirante/', views.ArchivosAspiranteApiView.as_view(), name='archivos aspirante api'),
     path('archivosaspirante/<int:pk>', ArchivosAspiranteApiView.as_view()),
   
]