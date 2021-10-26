from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .models import Ramaactividad
from rest_framework.generics import get_object_or_404

from .serializers import RamaactividadSerializer

from rest_framework.response import Response



# Create your views here.

class RamaactividadApiView(APIView):

  def get(self, request, pk=None):
        if pk:
            ramaactividad = get_object_or_404(Ramaactividad.objects.all(), pk=pk)
            serializer = RamaactividadSerializer(ramaactividad)
            return Response(serializer.data)
        ramaactividads = Ramaactividad.objects.all()
        serializer = RamaactividadSerializer(ramaactividads, many=True)
        return Response( serializer.data)

  def post(self, request):
        ramaactividad = request.data
        serializer = RamaactividadSerializer(data=ramaactividad)
        if serializer.is_valid(raise_exception=True):
            ramaactividad_saved = serializer.save()
        return Response({"success": "Ramaactividad '{}' created successfully".format(ramaactividad_saved.descripcion)})
  
  def put(self, request, pk):
        saved_ramaactividad = get_object_or_404(Ramaactividad.objects.all(), pk=pk)
        data = request.data
        serializer = RamaactividadSerializer(instance=saved_ramaactividad, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            ramaactividad_saved = serializer.save()
        return Response({"success": "Ramaactividad '{}' updated successfully".format(ramaactividad_saved.descripcion)})
  
  def delete(self, request, pk):
        ramaactividad = get_object_or_404(Ramaactividad.objects.all(), pk=pk)
        ramaactividad.delete()
        return Response({"message": "Ramaactividad with id `{}` has been deleted.".format(pk)},status=204)