from applications.NivelEstudios.serializers import EstadoEstudiosSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('nivelestudios/', views.NivelEstudiosApiView.as_view(), name='nivel estudios api'),
     path('nivelestudios/<int:pk>', NivelEstudiosApiView.as_view()),
   
]