from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Tiposolicitud
from .serializers import TiposolicitudSerializer

from rest_framework.response import Response


# Create your views here.

class TiposolicitudApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            tiposolicitud = get_object_or_404(Tiposolicitud.objects.all(), pk=pk)
            serializer = TiposolicitudSerializer(tiposolicitud)
            return Response(serializer.data)
        tiposolicituds = Tiposolicitud.objects.all()
        serializer = TiposolicitudSerializer(tiposolicituds, many=True)
        return Response(serializer.data)

  def post(self, request):
        tiposolicitud = request.data
        serializer = TiposolicitudSerializer(data=tiposolicitud)
        if serializer.is_valid(raise_exception=True):
           tiposolicitud_saved = serializer.save()
        return Response({"success": "Tiposolicitud '{}' created successfully".format(tiposolicitud_saved.descrpcion)})
  
  def put(self, request, pk):
        saved_tiposolicitud = get_object_or_404(Tiposolicitud.objects.all(), pk=pk)
        data = request.data
        serializer = TiposolicitudSerializer(instance=saved_tiposolicitud, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            tiposolicitud_saved = serializer.save()
        return Response({"success": "Tiposolicitud '{}' updated successfully".format(tiposolicitud_saved.descrpcion)})
  
  def delete(self, request, pk):
        tiposolicitud = get_object_or_404(Tiposolicitud.objects.all(), pk=pk)
        tiposolicitud.delete()
        return Response({"message": "Tipoempresa with id `{}` has been deleted.".format(pk)},status=204)