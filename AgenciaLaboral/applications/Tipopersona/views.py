from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Tipopersona
from .serializers import TipopersonaSerializer

from rest_framework.response import Response


# Create your views here.

class TipopersonaApiView(APIView):
   
  
  def get(self, request, pk=None):
        if pk:
            tipopersona = get_object_or_404(Tipopersona.objects.all(), pk=pk)
            serializer = TipopersonaSerializer(tipopersona)
            return Response(serializer.data)
        tipopersonas = Tipopersona.objects.all()
        serializer = TipopersonaSerializer(tipopersonas, many=True)
        return Response(serializer.data)

  def post(self, request):
        tipopersona = request.data
        serializer = TipopersonaSerializer(data=tipopersona)
        if serializer.is_valid(raise_exception=True):
            tipopersona_saved = serializer.save()
        return Response({"success": "Tipopersona '{}' created successfully".format(tipopersona_saved.descripcion)})
  
  def put(self, request, pk):
        saved_tipopersona = get_object_or_404(Tipopersona.objects.all(), pk=pk)
        data = request.data
        serializer = TipopersonaSerializer(instance=saved_tipopersona, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            tipopersona_saved = serializer.save()
        return Response({"success": "Tipopersona '{}' updated successfully".format(tipopersona_saved.descripcion)})
  
  def delete(self, request, pk):
        tipopersona = get_object_or_404(Tipopersona.objects.all(), pk=pk)
        tipopersona.delete()
        return Response({"message": "Tipoempresa with id `{}` has been deleted.".format(pk)},status=204)