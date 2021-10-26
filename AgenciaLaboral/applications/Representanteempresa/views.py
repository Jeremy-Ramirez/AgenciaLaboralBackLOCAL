from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Representanteempresa
from .serializers import RepresentanteEmpresaSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
# Create your views here.

class RepresentanteEmpresaApiView(APIView):


  def post(self, request, format=None):
        representanteempresa_serializer = RepresentanteEmpresaSerializer(data=request.data)
        if representanteempresa_serializer.is_valid():
            representanteempresa_serializer.save()
            return Response(representanteempresa_serializer.data, status=status.HTTP_201_CREATED)
        return Response(representanteempresa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self,request, pk=None, format=None):
        if pk:
            representanteempresa= get_object_or_404(Representanteempresa.objects.all(),pk=pk)
            representanteempresa_serializer = RepresentanteEmpresaSerializer(representanteempresa, many=False)
            return Response(representanteempresa_serializer.data)
        representantesempresa= Representanteempresa.objects.all()
        representanteempresa_serializer=RepresentanteEmpresaSerializer(representantesempresa,many=True)
        return Response(representanteempresa_serializer.data)

