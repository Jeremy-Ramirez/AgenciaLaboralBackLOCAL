from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Sector
from .serializers import SectorSerializer

from rest_framework.response import Response


# Create your views here.

class SectorApiView(APIView):
   
  
  def get(self, request, pk=None):
        if pk:
            sector = get_object_or_404(Sector.objects.all(), pk=pk)
            serializer = SectorSerializer(sector)
            return Response(serializer.data)
        sectors = Sector.objects.all()
        serializer = SectorSerializer(sectors, many=True)
        return Response(serializer.data)

  def post(self, request):
        sector = request.data
        serializer = SectorSerializer(data=sector)
        if serializer.is_valid(raise_exception=True):
            sector_saved = serializer.save()
        return Response({"success": "Sector '{}' created successfully".format(sector_saved.descripcion)})
  
  def put(self, request, pk):
        saved_sector = get_object_or_404(Sector.objects.all(), pk=pk)
        data = request.data
        serializer = SectorSerializer(instance=saved_sector, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            sector_saved = serializer.save()
        return Response({"success": "Sector '{}' updated successfully".format(sector_saved.descripcion)})
  
  def delete(self, request, pk):
        sector = get_object_or_404(Sector.objects.all(), pk=pk)
        sector.delete()
        return Response({"message": "Sector with id `{}` has been deleted.".format(pk)},status=204)