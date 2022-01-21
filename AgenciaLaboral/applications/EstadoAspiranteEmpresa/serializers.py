from rest_framework import serializers
from .models import EstadoAspiranteEmpresa


class EstadoAspiranteEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstadoAspiranteEmpresa
        fields='__all__'
    
    def create(self,validated_data):
            return EstadoAspiranteEmpresa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idestadoaspiranteempresa = validated_data.get('idestadoaspiranteempresa', instance.idestadoaspiranteempresa)
        instance.estado = validated_data.get('estado', instance.estado)
        
        instance.save()
        return instance