
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import SugerenciaEmpresa
from rest_framework.views import APIView


class SugerenciaEmpresaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=SugerenciaEmpresa
        fields=("idsugerenciaempresa","titulo","descripcion","imagen","empresa_idempresa")

    def create(self,validated_data):
        return SugerenciaEmpresa.objects.create(**validated_data)