from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Solicitud
from .serializers import SolicitudSerializer

from rest_framework.response import Response


# Create your views here.

class SolicitudApiView(APIView):
   
  
  def get(self, request, pk=None):
        if pk:
            solicitud = get_object_or_404(Solicitud.objects.all(), pk=pk)
            serializer = SolicitudSerializer(solicitud)
            return Response(serializer.data)
        solicituds = Solicitud.objects.all()
        serializer = SolicitudSerializer(solicituds, many=True)
        return Response(serializer.data)

  def post(self, request):
        solicitud = request.data
        serializer = SolicitudSerializer(data=solicitud)
        if serializer.is_valid(raise_exception=True):
            solicitud_saved = serializer.save()
        return Response({"success": "Solicitud '{}' created successfully".format(solicitud_saved.descripcion)})
  
  def put(self, request, pk):
        saved_solicitud = get_object_or_404(Solicitud.objects.all(), pk=pk)
        data = request.data
        serializer = SolicitudSerializer(instance=saved_solicitud, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            solicitud_saved = serializer.save()
        return Response({"success": "Solicitud '{}' updated successfully".format(solicitud_saved.descripcion)})
  
  def delete(self, request, pk):
        solicitud = get_object_or_404(Solicitud.objects.all(), pk=pk)
        solicitud.delete()
        return Response({"message": "Solicitud with id `{}` has been deleted.".format(pk)},status=204)