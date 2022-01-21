from django.shortcuts import render

# Create your views here.
from .models import Paquetepago
from rest_framework.response import Response
from .serializers import PaquetepagoSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404


# Create your views here.

class PaquetepagoApiView(APIView):
  
  def post(self, request):
      #if request.method == 'POST':
        paquetepago_serializer = PaquetepagoSerializer(data=request.data)
        if paquetepago_serializer.is_valid():
            paquetepago_serializer.save()
            return Response(paquetepago_serializer.data, status=status.HTTP_201_CREATED)
        return Response(paquetepago_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self,request, pk=None, format=None):
        if pk:
            paquetepago= get_object_or_404(Paquetepago.objects.all(),pk=pk)
            paquetepago_serializer = PaquetepagoSerializer(paquetepago, many=False)
            return Response(paquetepago_serializer.data)
        paquetepagos= Paquetepago.objects.all()
        paquetepagos_serializer=PaquetepagoSerializer(paquetepagos,many=True)
        return Response(paquetepagos_serializer.data)

  def put(self, request, pk):
        paquetepago = get_object_or_404(Paquetepago.objects.all(),pk=pk)
        paquetepago_serializer = PaquetepagoSerializer(paquetepago, data=request.data, many=False)
        if paquetepago_serializer.is_valid(raise_exception=True):
            paquetepago_serializer.save()
            return Response(paquetepago_serializer.data)
        return Response(paquetepago_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk):
        paquetepago = get_object_or_404(Paquetepago.objects.all(),pk=pk)
        paquetepago_serializer = PaquetepagoSerializer(paquetepago, data=request.data, partial=True) # set partial=True to update a data partially
        if paquetepago_serializer.is_valid():
            paquetepago_serializer.save()
            return Response(paquetepago_serializer.data)
        return Response(paquetepago_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
        paquetepago = get_object_or_404(Paquetepago.objects.all(), pk=pk)
        paquetepago.delete()
        return Response({"message": "El paquete de pago_serializer con id `{}` ha sido eliminado.".format(pk)},status=204)
