from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Estado
from .serializers import EstadoSerializer
from rest_framework.response import Response


class EstadoApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            estado = get_object_or_404(Estado.objects.all(), pk=pk)
            serializer = EstadoSerializer(estado)
            return Response( serializer.data)
        estados = Estado.objects.all()
        serializer = EstadoSerializer(estados, many=True)
        return Response(serializer.data)

  def post(self, request):
        estado = request.data
        serializer = EstadoSerializer(data=estado)
        if serializer.is_valid(raise_exception=True):
            estado_saved = serializer.save()
        return Response({"success": "Estado '{}' created successfully".format(estado_saved.estado)})
  
  def put(self, request, pk):
        saved_estado = get_object_or_404(Estado.objects.all(), pk=pk)
        data = request.data
        serializer = EstadoSerializer(instance=saved_estado, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            estado_saved = serializer.save()
        return Response({"success": "Estado '{}' updated successfully".format(estado_saved.estado)})
  
  def delete(self, request, pk):
        estado = get_object_or_404(Estado.objects.all(), pk=pk)
        estado.delete()
        return Response({"message": "Estado with id `{}` has been deleted.".format(pk)},status=204)