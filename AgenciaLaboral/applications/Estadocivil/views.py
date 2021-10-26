from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Estadocivil
from .serializers import EstadocivilSerializer
from rest_framework.response import Response


class EstadocivilApiView(APIView):
   
  def get(self, request, pk=None):
        if pk:
            estadocivil = get_object_or_404(Estadocivil.objects.all(), pk=pk)
            serializer = EstadocivilSerializer(estadocivil)
            return Response( serializer.data)
        estadocivils = Estadocivil.objects.all()
        serializer = EstadocivilSerializer(estadocivils, many=True)
        return Response(serializer.data)

  def post(self, request):
        estadocivil = request.data
        serializer = EstadocivilSerializer(data=estadocivil)
        if serializer.is_valid(raise_exception=True):
            estadocivil_saved = serializer.save()
        return Response({"success": "Estadocivil '{}' created successfully".format(estadocivil_saved.estadocivil)})
  
  def put(self, request, pk):
        saved_estadocivil = get_object_or_404(Estadocivil.objects.all(), pk=pk)
        data = request.data
        serializer = EstadocivilSerializer(instance=saved_estadocivil, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            estadocivil_saved = serializer.save()
        return Response({"success": "Estadocivil '{}' updated successfully".format(estadocivil_saved.estadocivil)})
  
  def delete(self, request, pk):
        estadocivil = get_object_or_404(Estadocivil.objects.all(), pk=pk)
        estadocivil.delete()
        return Response({"message": "Estadocivil with id `{}` has been deleted.".format(pk)},status=204)