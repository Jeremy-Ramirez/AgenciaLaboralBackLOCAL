from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Provincia
from .serializers import ProvinciaSerializer

from rest_framework.response import Response


# Create your views here.

class ProvinciaApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            provincia = get_object_or_404(Provincia.objects.all(), pk=pk)
            serializer = ProvinciaSerializer(provincia)
            return Response(serializer.data)
        provincias = Provincia.objects.all()
        serializer = ProvinciaSerializer(provincias, many=True)
        return Response(serializer.data)

  def post(self, request):
        provincia = request.data
        serializer = ProvinciaSerializer(data=provincia)
        if serializer.is_valid(raise_exception=True):
            provincia_saved = serializer.save()
        return Response({"success": "Provincia '{}' created successfully".format(provincia_saved.nombreprovincia)})
  
  def put(self, request, pk):
        saved_provincia = get_object_or_404(Provincia.objects.all(), pk=pk)
        data = request.data
        serializer = ProvinciaSerializer(instance=saved_provincia, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            provincia_saved = serializer.save()
        return Response({"success": "Provincia '{}' updated successfully".format(provincia_saved.nombreprovincia)})
  
  def delete(self, request, pk):
        provincia = get_object_or_404(Provincia.objects.all(), pk=pk)
        provincia.delete()
        return Response({"message": "Provincia with id `{}` has been deleted.".format(pk)},status=204)