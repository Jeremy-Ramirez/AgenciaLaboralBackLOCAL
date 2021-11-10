from django.shortcuts import render

# Create your views here.
from .models import SugerenciaEmpresa
from rest_framework.response import Response
from .serializers import SugerenciaEmpresaSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

#from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# Create your views here.

class SugerenciaEmpresaApiView(APIView):
  queryset = SugerenciaEmpresa.objects.all()
  serializer_class = SugerenciaEmpresaSerializer
  #parser_classes = (MultiPartParser,FormParser,JSONParser)
  
  def post(self, request, *args, **kwargs):
    sugerenciaEmpresa_serializer = SugerenciaEmpresaSerializer(data=request.data)
    if sugerenciaEmpresa_serializer.is_valid():
      sugerenciaEmpresa_serializer.save()
      return Response(sugerenciaEmpresa_serializer.data, status=status.HTTP_201_CREATED)
    return Response(sugerenciaEmpresa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self,request, pk=None, format=None):
        if pk:
            sugerenciaEmpresa= get_object_or_404(SugerenciaEmpresa.objects.all(),pk=pk)
            sugerenciaEmpresa_serializer = SugerenciaEmpresaSerializer(sugerenciaEmpresa, many=False)
            return Response(sugerenciaEmpresa_serializer.data)
        sugerenciasEmpresa= SugerenciaEmpresa.objects.all()
        sugerenciaEmpresa_serializer=SugerenciaEmpresaSerializer(sugerenciasEmpresa,many=True)
        return Response(sugerenciaEmpresa_serializer.data)