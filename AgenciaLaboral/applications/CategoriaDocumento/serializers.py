
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import CategoriaDocumento
from rest_framework.views import APIView

class CategoriaDocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model=CategoriaDocumento
        fields='__all__'

    def create(self,validated_data):
        return CategoriaDocumento.objects.create(**validated_data)