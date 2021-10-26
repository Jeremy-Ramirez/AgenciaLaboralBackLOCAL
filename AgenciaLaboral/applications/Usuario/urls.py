from applications.Usuario.serializers import UsuarioSerializer
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
  
     path('usuarios/', views.UsuarioApiView.as_view(), name='usuarios api'),
     path('usuarios/<int:pk>', views.UsuarioApiView.as_view()),
     path('loginusuario/', LoginView.as_view()),
     path('userusuario/', UsuarioView.as_view()),
     path('logoutusuario/', LogoutView.as_view())
   
]
