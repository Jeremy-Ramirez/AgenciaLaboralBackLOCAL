
from rest_framework import serializers
from .models import Profesiones


class ProfesionesSerializer(serializers.ModelSerializer):

     class Meta:
        model=Profesiones
        fields='__all__'