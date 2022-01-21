from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import EstadoAspiranteEmpresa
from .serializers import EstadoAspiranteEmpresaSerializer
from rest_framework.response import Response


class EstadoAspiranteEmpresaApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            estado = get_object_or_404(EstadoAspiranteEmpresa.objects.all(), pk=pk)
            serializer = EstadoAspiranteEmpresaSerializer(estado)
            return Response( serializer.data)
        estados = EstadoAspiranteEmpresa.objects.all()
        serializer = EstadoAspiranteEmpresaSerializer(estados, many=True)
        return Response(serializer.data)

  def post(self, request):
        estado = request.data
        serializer = EstadoAspiranteEmpresaSerializer(data=estado)
        if serializer.is_valid(raise_exception=True):
            estado_saved = serializer.save()
        return Response({"success": "EstadoAspiranteEmpresas '{}' created successfully".format(estado_saved.estado)})
  
  def put(self, request, pk):
        saved_estado = get_object_or_404(EstadoAspiranteEmpresa.objects.all(), pk=pk)
        data = request.data
        serializer = EstadoAspiranteEmpresaSerializer(instance=saved_estado, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            estado_saved = serializer.save()
        return Response({"success": "EstadoAspiranteEmpresa '{}' updated successfully".format(estado_saved.estado)})
  
  def delete(self, request, pk):
        estado = get_object_or_404(EstadoAspiranteEmpresa.objects.all(), pk=pk)
        estado.delete()
        return Response({"message": "EstadoAspiranteEmpresa with id `{}` has been deleted.".format(pk)},status=204)
