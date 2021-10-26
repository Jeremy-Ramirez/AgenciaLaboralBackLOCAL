from django.shortcuts import render

# Create your views here.
from .models import Aspirante
from rest_framework.response import Response
from .serializers import AspiranteSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404


class AspiranteApiView(APIView):

    def get(self,request, pk=None, format=None):
        if pk:
            aspirante= get_object_or_404(Aspirante.objects.all(),pk=pk)
            aspirante_serializer = AspiranteSerializer(aspirante, many=False)
            return Response(aspirante_serializer.data)
        aspirantes= Aspirante.objects.all()
        aspirantes_serializer=AspiranteSerializer(aspirantes,many=True)
        return Response(aspirantes_serializer.data)


    def post(self, request):
     
        aspirante_serializer = AspiranteSerializer(data=request.data)
        if aspirante_serializer.is_valid():
            aspirante_serializer.save()
            return Response(aspirante_serializer.data, status=status.HTTP_201_CREATED)
        return Response(aspirante_serializer.errors, status=status.HTTP_400_BAD_REQUEST)