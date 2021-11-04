
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import NivelEstudios
from rest_framework.views import APIView

class NivelEstudiosSerializer(serializers.ModelSerializer):

    class Meta:
        model=NivelEstudios
        fields='__all__'

    def create(self,validated_data):
        return NivelEstudios.objects.create(**validated_data)