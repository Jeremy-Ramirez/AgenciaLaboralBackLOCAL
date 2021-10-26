from django.shortcuts import render

from .models import Profesiones
from rest_framework.response import Response
from .serializers import ProfesionesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404


class ProfesionesApiView(APIView):

   def get(self,request, format=None):
      profesiones= Profesiones.objects.all()
      profesiones_serializer=ProfesionesSerializer(profesiones,many=True)
      return Response(profesiones_serializer.data)