from django.shortcuts import render

# Create your views here.
from .models import CategoriaDocumento
from rest_framework.response import Response
from .serializers import CategoriaDocumentoSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404


# Create your views here.

class CategoriaDocumentoApiView(APIView):
  
  def post(self, request):
      #if request.method == 'POST':
        categoriadocumento_serializer = CategoriaDocumentoSerializer(data=request.data)
        if categoriadocumento_serializer.is_valid():
            categoriadocumento_serializer.save()
            return Response(categoriadocumento_serializer.data, status=status.HTTP_201_CREATED)
        return Response(categoriadocumento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self,request, pk=None, format=None):
        if pk:
            categoriadocumento= get_object_or_404(CategoriaDocumento.objects.all(),pk=pk)
            categoriadocumento_serializer = CategoriaDocumentoSerializer(categoriadocumento, many=False)
            return Response(categoriadocumento_serializer.data)
        categoriasdocumentos= CategoriaDocumento.objects.all()
        categoriadocumento_serializer=CategoriaDocumentoSerializer(categoriasdocumentos,many=True)
        return Response(categoriadocumento_serializer.data)

  def put(self, request, pk):
        categoriadocumento = get_object_or_404(CategoriaDocumento.objects.all(),pk=pk)
        categoriadocumento_serializer = CategoriaDocumentoSerializer(categoriadocumento, data=request.data, many=False)
        if categoriadocumento_serializer.is_valid(raise_exception=True):
            categoriadocumento_serializer.save()
            return Response(categoriadocumento_serializer.data)
        return Response(categoriadocumento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)