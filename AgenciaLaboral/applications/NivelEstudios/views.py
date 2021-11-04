from django.shortcuts import render

# Create your views here.
from .models import NivelEstudios
from rest_framework.response import Response
from .serializers import NivelEstudiosSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404


# Create your views here.

class NivelEstudiosApiView(APIView):
  
  def post(self, request):
      #if request.method == 'POST':
        nivelestudios_serializer = NivelEstudiosSerializer(data=request.data)
        if nivelestudios_serializer.is_valid():
            nivelestudios_serializer.save()
            return Response(nivelestudios_serializer.data, status=status.HTTP_201_CREATED)
        return Response(nivelestudios_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self,request, pk=None, format=None):
        if pk:
            nivelestudios= get_object_or_404(NivelEstudios.objects.all(),pk=pk)
            nivelestudios_serializer = NivelEstudiosSerializer(nivelestudios, many=False)
            return Response(nivelestudios_serializer.data)
        nivelsestudios= NivelEstudios.objects.all()
        nivelestudios_serializer=NivelEstudiosSerializer(nivelsestudios,many=True)
        return Response(nivelestudios_serializer.data)

  def put(self, request, pk):
        nivelestudios = get_object_or_404(NivelEstudios.objects.all(),pk=pk)
        nivelestudios_serializer = NivelEstudiosSerializer(nivelestudios, data=request.data, many=False)
        if nivelestudios_serializer.is_valid(raise_exception=True):
            nivelestudios_serializer.save()
            return Response(nivelestudios_serializer.data)
        return Response(nivelestudios_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
