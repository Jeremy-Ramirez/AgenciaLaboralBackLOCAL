
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import DuracionPaquetes
from rest_framework.views import APIView

class DuracionPaquetesSerializer(serializers.ModelSerializer):

    class Meta:
        model=DuracionPaquetes
        fields='__all__'

    def create(self,validated_data):
        return DuracionPaquetes.objects.create(**validated_data)