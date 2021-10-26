
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import Sugerencia
from rest_framework.views import APIView


class SugerenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Sugerencia
        fields=("idsugerencia","titulo","descripcion","imagen","usuario_idusuario")

    def create(self,validated_data):
        return Sugerencia.objects.create(**validated_data)
