
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import ArchivosAspirante
from rest_framework.views import APIView

class ArchivosAspirantesSerializer(serializers.ModelSerializer):

    class Meta:
        model=ArchivosAspirante
        fields='__all__'

    def create(self,validated_data):
        return ArchivosAspirante.objects.create(**validated_data)