from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Actividadeconomica
from .serializers import ActividadeconomicaSerializer

from rest_framework.response import Response

class ActividadeconomicaApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            actividadeconomica = get_object_or_404(Actividadeconomica.objects.all(), pk=pk)
            serializer = ActividadeconomicaSerializer(actividadeconomica)
            return Response(serializer.data)
        actividadeconomicas = Actividadeconomica.objects.all()
        serializer = ActividadeconomicaSerializer(actividadeconomicas, many=True)
        return Response(serializer.data)

  def post(self, request):
        actividadeconomica = request.data
        serializer = ActividadeconomicaSerializer(data=actividadeconomica)
        if serializer.is_valid(raise_exception=True):
            actividadeconomica_saved = serializer.save()
        return Response({"success": "Actividadeconomica '{}' created successfully".format(actividadeconomica_saved.descripcion)})
  
  def put(self, request, pk):
        saved_actividadeconomica = get_object_or_404(Actividadeconomica.objects.all(), pk=pk)
        data = request.data
        serializer = ActividadeconomicaSerializer(instance=saved_actividadeconomica, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            actividadeconomica_saved = serializer.save()
        return Response({"success": "Actividadeconomica '{}' updated successfully".format(actividadeconomica_saved.descripcion)})
  
  def delete(self, request, pk):
        actividadeconomica = get_object_or_404(Actividadeconomica.objects.all(), pk=pk)
        actividadeconomica.delete()
        return Response({"message": "Actividadeconomica with id `{}` has been deleted.".format(pk)},status=204)