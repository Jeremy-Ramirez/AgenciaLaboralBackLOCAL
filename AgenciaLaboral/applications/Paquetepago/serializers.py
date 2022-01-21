
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import Paquetepago
from rest_framework.views import APIView

class PaquetepagoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Paquetepago
        fields='__all__'

    def create(self,validated_data):
        return Paquetepago.objects.create(**validated_data)