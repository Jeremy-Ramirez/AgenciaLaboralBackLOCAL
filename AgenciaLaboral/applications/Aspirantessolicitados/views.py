from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Aspirantessolicitados
from .serializers import AspirantessolicitadosSerializer

from rest_framework.response import Response

# Create your views here.

class AspirantessolicitadosApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            aspirantessolicitados = get_object_or_404(Aspirantessolicitados.objects.all(), pk=pk)
            serializer = AspirantessolicitadosSerializer(aspirantessolicitados, many=False)
            return Response(serializer.data)
        aspirantessolicitadoss = Aspirantessolicitados.objects.all()
        serializer = AspirantessolicitadosSerializer(aspirantessolicitadoss, many=True)
        return Response(serializer.data)

  def post(self, request):
        aspirantessolicitados = request.data
        serializer = AspirantessolicitadosSerializer(data=aspirantessolicitados)
        if serializer.is_valid(raise_exception=True):
            aspirantessolicitados_saved = serializer.save()
        return Response({"success": "Aspirantessolicitados '{}' created successfully".format(aspirantessolicitados_saved.idaspirantessolicitados)})
  
  def put(self, request, pk):
        saved_aspirantessolicitados = get_object_or_404(Aspirantessolicitados.objects.all(), pk=pk)
        data = request.data
        serializer = AspirantessolicitadosSerializer(instance=saved_aspirantessolicitados, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            aspirantessolicitados_saved = serializer.save()
        return Response({"success": "Aspirantessolicitados '{}' updated successfully".format(aspirantessolicitados_saved.idaspirantessolicitados)})
  
  def delete(self, request, pk):
        aspirantessolicitados = get_object_or_404(Aspirantessolicitados.objects.all(), pk=pk)
        aspirantessolicitados.delete()
        return Response({"message": "Aspirantessolicitados with id `{}` has been deleted.".format(pk)},status=204)