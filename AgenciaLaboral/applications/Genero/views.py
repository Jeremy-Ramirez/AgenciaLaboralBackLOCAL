from django.shortcuts import render





from rest_framework.views import APIView
from .models import Genero
from .serializers import GeneroSerializer

from rest_framework.response import Response



# Create your views here.

class GeneroApiView(APIView):
   

  def get(self,request, format=None):
      generos= Genero.objects.all()
      genero_serializer=GeneroSerializer(generos,many=True)
      return Response(genero_serializer.data)




