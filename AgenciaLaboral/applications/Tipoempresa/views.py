from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Tipoempresa
from .serializers import TipoempresaSerializer
from rest_framework.response import Response


# Create your views here.

class TipoempresaApiView(APIView):
   
  
  def get(self, request, pk=None):
        if pk:
            tipoempresa = get_object_or_404(Tipoempresa.objects.all(), pk=pk)
            serializer = TipoempresaSerializer(tipoempresa)
            return Response(serializer.data)
        tipoempresas = Tipoempresa.objects.all()
        serializer = TipoempresaSerializer(tipoempresas, many=True)
        return Response(serializer.data)

  def post(self, request):
        tipoempresa = request.data
        serializer = TipoempresaSerializer(data=tipoempresa)
        if serializer.is_valid(raise_exception=True):
            tipoempresa_saved = serializer.save()
        return Response({"success": "Tipoempresa '{}' created successfully".format(tipoempresa_saved.descripcion)})
  
  def put(self, request, pk):
        saved_tipoempresa = get_object_or_404(Tipoempresa.objects.all(), pk=pk)
        data = request.data
        serializer = TipoempresaSerializer(instance=saved_tipoempresa, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            tipoempresa_saved = serializer.save()
        return Response({"success": "Tipoempresa '{}' updated successfully".format(tipoempresa_saved.descripcion)})
  
  def delete(self, request, pk):
        tipoempresa = get_object_or_404(Tipoempresa.objects.all(), pk=pk)
        tipoempresa.delete()
        return Response({"message": "Tipoempresa with id `{}` has been deleted.".format(pk)},status=204)