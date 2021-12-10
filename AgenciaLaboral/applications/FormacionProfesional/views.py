from django.shortcuts import render

# Create your views here.
from .models import FormacionProfesional
from rest_framework.response import Response
from .serializers import FormacionProfesionalSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404


# Create your views here.

class FormacionProfesionalApiView(APIView):
  
  


  def get(self,request, pk=None, format=None):
        if pk:
            formacionProfesional= get_object_or_404(FormacionProfesional.objects.all(),pk=pk)
            formacionProfesional_serializer = FormacionProfesionalSerializer(formacionProfesional, many=False)
            return Response(formacionProfesional_serializer.data)
        formacionesProfesionales= FormacionProfesional.objects.all()
        formacionesProfesionales_serializer=FormacionProfesionalSerializer(formacionesProfesionales,many=True)
        return Response(formacionesProfesionales_serializer.data)
        
  def post(self, request):
      #if request.method == 'POST':
        formacionProfesional_serializer = FormacionProfesionalSerializer(data=request.data)
        if formacionProfesional_serializer.is_valid():
            formacionProfesional_serializer.save()
            return Response(formacionProfesional_serializer.data, status=status.HTTP_201_CREATED)
        return Response(formacionProfesional_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk):
        formacionProfesional = get_object_or_404(FormacionProfesional.objects.all(),pk=pk)
        formacionProfesional_serializer = FormacionProfesionalSerializer(formacionProfesional, data=request.data, many=False)
        if formacionProfesional_serializer.is_valid(raise_exception=True):
            formacionProfesional_serializer.save()
            return Response(formacionProfesional_serializer.data)
        return Response(formacionProfesional_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
        formacionProfesional = get_object_or_404(FormacionProfesional.objects.all(), pk=pk)
        formacionProfesional.delete()
        return Response({"message": "La formación profesional con el id `{}` ha sido eliminada.".format(pk)},status=204)