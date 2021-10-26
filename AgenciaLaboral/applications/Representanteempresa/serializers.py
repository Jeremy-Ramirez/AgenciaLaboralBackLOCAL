
from rest_framework import serializers
from .models import Representanteempresa
from rest_framework.views import APIView

class RepresentanteEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Representanteempresa
        fields='__all__'

    def create(self,validated_data):
        return Representanteempresa.objects.create(**validated_data)