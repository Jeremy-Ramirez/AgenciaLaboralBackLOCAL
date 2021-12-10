from rest_framework import serializers
from .models import EstadoAspirantes


class EstadoAspirantesSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstadoAspirantes
        fields='__all__'
    
    def create(self,validated_data):
            return EstadoAspirantes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idestadoaspirantes = validated_data.get('idestadoaspirantes', instance.idestadoaspirantes)
        instance.estado = validated_data.get('estado', instance.estado)
        
        instance.save()
        return instance