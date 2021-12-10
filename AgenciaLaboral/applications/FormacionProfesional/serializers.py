
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import FormacionProfesional
from rest_framework.views import APIView

class FormacionProfesionalSerializer(serializers.ModelSerializer):

    class Meta:
        model=FormacionProfesional
        fields='__all__'

    def create(self,validated_data):
        return FormacionProfesional.objects.create(**validated_data)