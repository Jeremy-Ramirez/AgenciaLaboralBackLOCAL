from applications.FormacionProfesional.serializers import FormacionProfesionalSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('formacionprofesional/', FormacionProfesionalApiView.as_view(), name='formación profesional api'),
     path('formacionprofesional/<int:pk>', FormacionProfesionalApiView.as_view()),
   
]