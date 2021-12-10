from django.shortcuts import render

# Create your views here.
from .models import ArchivosAspirante
from rest_framework.response import Response
from .serializers import ArchivosAspirantesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404


# Create your views here.

class ArchivosAspiranteApiView(APIView):
  
  def post(self, request):
      #if request.method == 'POST':
        archivosAspirantes_serializer = ArchivosAspirantesSerializer(data=request.data)
        if archivosAspirantes_serializer.is_valid():
            archivosAspirantes_serializer.save()
            return Response(archivosAspirantes_serializer.data, status=status.HTTP_201_CREATED)
        return Response(archivosAspirantes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self,request, pk=None, format=None):
        if pk:
            archivoAspirante= get_object_or_404(ArchivosAspirante.objects.all(),pk=pk)
            archivosAspirantes_serializer = ArchivosAspirantesSerializer(archivoAspirante, many=False)
            return Response(archivosAspirantes_serializer.data)
        archivosAspirantes= ArchivosAspirante.objects.all()
        archivosAspirantes_serializer=ArchivosAspirantesSerializer(archivosAspirantes,many=True)
        return Response(archivosAspirantes_serializer.data)

  def put(self, request, pk):
        usuario = get_object_or_404(ArchivosAspirante.objects.all(),pk=pk)
        archivosAspirantes_serializer = ArchivosAspirantesSerializer(usuario, data=request.data, many=False)
        if archivosAspirantes_serializer.is_valid(raise_exception=True):
            archivosAspirantes_serializer.save()
            return Response(archivosAspirantes_serializer.data)
        return Response(archivosAspirantes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
        archivoAspirante = get_object_or_404(ArchivosAspirante.objects.all(), pk=pk)
        archivoAspirante.delete()
        return Response({"message": "El archivo con id `{}` ha sido eliminado.".format(pk)},status=204)