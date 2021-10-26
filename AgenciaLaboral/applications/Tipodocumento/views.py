from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Tipodocumento
from .serializers import TipodocumentoSerializer

from rest_framework.response import Response



# Create your views here.

class TipodocumentoApiView(APIView):

  def get(self, request, pk=None):
        if pk:
            tipodocumento = get_object_or_404(Tipodocumento.objects.all(), pk=pk)
            serializer = TipodocumentoSerializer(tipodocumento)
            return Response(serializer.data)
        tipodocumentos = Tipodocumento.objects.all()
        serializer = TipodocumentoSerializer(tipodocumentos, many=True)
        return Response(serializer.data)

  def post(self, request):
        tipodocumento = request.data
        serializer = TipodocumentoSerializer(data=tipodocumento)
        if serializer.is_valid(raise_exception=True):
            tipodocumento_saved = serializer.save()
        return Response({"success": "Tipodocumento '{}' created successfully".format(tipodocumento_saved.descripcion)})
  
  def put(self, request, pk):
        saved_tipodocumento = get_object_or_404(Tipodocumento.objects.all(), pk=pk)
        data = request.data
        serializer = TipodocumentoSerializer(instance=saved_tipodocumento, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            tipodocumento_saved = serializer.save()
        return Response({"success": "Tipodocumento '{}' updated successfully".format(tipodocumento_saved.descripcion)})
  
  def delete(self, request, pk):
        tipodocumento = get_object_or_404(Tipodocumento.objects.all(), pk=pk)
        tipodocumento.delete()
        return Response({"message": "Tipodocumento with id `{}` has been deleted.".format(pk)},status=204)