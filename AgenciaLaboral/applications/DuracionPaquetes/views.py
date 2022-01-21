from django.shortcuts import render

# Create your views here.
from .models import DuracionPaquetes
from rest_framework.response import Response
from .serializers import DuracionPaquetesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404


# Create your views here.

class DuracionPaquetesApiView(APIView):
  
  def post(self, request):
      #if request.method == 'POST':
        duracionpaquetes_serializer = DuracionPaquetesSerializer(data=request.data)
        if duracionpaquetes_serializer.is_valid():
            duracionpaquetes_serializer.save()
            return Response(duracionpaquetes_serializer.data, status=status.HTTP_201_CREATED)
        return Response(duracionpaquetes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self,request, pk=None, format=None):
        if pk:
            duracionPaquete= get_object_or_404(DuracionPaquetes.objects.all(),pk=pk)
            duracionpaquetes_serializer = DuracionPaquetesSerializer(duracionPaquete, many=False)
            return Response(duracionpaquetes_serializer.data)
        duracionPaquetes= DuracionPaquetes.objects.all()
        duracionpaquetes_serializer=DuracionPaquetesSerializer(duracionPaquetes,many=True)
        return Response(duracionpaquetes_serializer.data)

  def put(self, request, pk):
        duracionPaquete = get_object_or_404(DuracionPaquetes.objects.all(),pk=pk)
        duracionpaquetes_serializer = DuracionPaquetesSerializer(duracionPaquete, data=request.data, many=False)
        if duracionpaquetes_serializer.is_valid(raise_exception=True):
            duracionpaquetes_serializer.save()
            return Response(duracionpaquetes_serializer.data)
        return Response(duracionpaquetes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
        duracionPaquetes = get_object_or_404(DuracionPaquetes.objects.all(), pk=pk)
        duracionPaquetes.delete()
        return Response({"message": "La duración del paquete con id `{}` ha sido eliminada.".format(pk)},status=204)
