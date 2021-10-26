from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Ciudad
from .serializers import CiudadSerializer

from rest_framework.response import Response

# Create your views here.

class CiudadApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            ciudad = get_object_or_404(Ciudad.objects.all(), pk=pk)
            serializer = CiudadSerializer(ciudad, many=False)
            return Response(serializer.data)
        Ciudads = Ciudad.objects.all()
        serializer = CiudadSerializer(Ciudads, many=True)
        return Response(serializer.data)

  def post(self, request):
        ciudad = request.data
        serializer = CiudadSerializer(data=ciudad)
        if serializer.is_valid(raise_exception=True):
            ciudad_saved = serializer.save()
        return Response({"success": "Ciudad '{}' created successfully".format(ciudad_saved.nombreciudad)})
  
  def put(self, request, pk):
        saved_ciudad = get_object_or_404(Ciudad.objects.all(), pk=pk)
        data = request.data
        serializer = CiudadSerializer(instance=saved_ciudad, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            ciudad_saved = serializer.save()
        return Response({"success": "Ciudad '{}' updated successfully".format(ciudad_saved.nombreciudad)})
  
  def delete(self, request, pk):
        ciudad = get_object_or_404(Ciudad.objects.all(), pk=pk)
        ciudad.delete()
        return Response({"message": "Ciudad with id `{}` has been deleted.".format(pk)},status=204)