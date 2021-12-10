from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import EstadoAspirantes
from .serializers import EstadoAspirantesSerializer
from rest_framework.response import Response


class EstadoAspirantesApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            estado = get_object_or_404(EstadoAspirantes.objects.all(), pk=pk)
            serializer = EstadoAspirantesSerializer(estado)
            return Response( serializer.data)
        estados = EstadoAspirantes.objects.all()
        serializer = EstadoAspirantesSerializer(estados, many=True)
        return Response(serializer.data)

  def post(self, request):
        estado = request.data
        serializer = EstadoAspirantesSerializer(data=estado)
        if serializer.is_valid(raise_exception=True):
            estado_saved = serializer.save()
        return Response({"success": "EstadoAspirantes '{}' created successfully".format(estado_saved.estado)})
  
  def put(self, request, pk):
        saved_estado = get_object_or_404(EstadoAspirantes.objects.all(), pk=pk)
        data = request.data
        serializer = EstadoAspirantesSerializer(instance=saved_estado, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            estado_saved = serializer.save()
        return Response({"success": "EstadoAspirantes '{}' updated successfully".format(estado_saved.estado)})
  
  def delete(self, request, pk):
        estado = get_object_or_404(EstadoAspirantes.objects.all(), pk=pk)
        estado.delete()
        return Response({"message": "EstadoAspirantes with id `{}` has been deleted.".format(pk)},status=204)
