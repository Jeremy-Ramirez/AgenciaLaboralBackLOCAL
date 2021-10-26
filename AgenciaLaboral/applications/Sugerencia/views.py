from django.shortcuts import render

# Create your views here.
from .models import Sugerencia
from rest_framework.response import Response
from .serializers import SugerenciaSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

#from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# Create your views here.

class SugerenciaApiView(APIView):
  queryset = Sugerencia.objects.all()
  serializer_class = SugerenciaSerializer
  #parser_classes = (MultiPartParser,FormParser,JSONParser)
  
  def post(self, request, *args, **kwargs):
    sugerencia_serializer = SugerenciaSerializer(data=request.data)
    if sugerencia_serializer.is_valid():
      sugerencia_serializer.save()
      return Response(sugerencia_serializer.data, status=status.HTTP_201_CREATED)
    return Response(sugerencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self,request, pk=None, format=None):
        if pk:
            sugerencia= get_object_or_404(Sugerencia.objects.all(),pk=pk)
            sugerencia_serializer = SugerenciaSerializer(sugerencia, many=False)
            return Response(sugerencia_serializer.data)
        sugerencias= Sugerencia.objects.all()
        sugerencia_serializer=SugerenciaSerializer(sugerencias,many=True)
        return Response(sugerencia_serializer.data)