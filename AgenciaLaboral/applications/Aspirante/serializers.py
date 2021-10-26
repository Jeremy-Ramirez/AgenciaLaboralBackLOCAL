from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import Aspirante
from rest_framework.views import APIView

class AspiranteSerializer(serializers.ModelSerializer):

    class Meta:
        model=Aspirante
        fields='__all__'

    def create(self,validated_data):
        return Aspirante.objects.create(**validated_data)