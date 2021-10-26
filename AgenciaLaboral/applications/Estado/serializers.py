from rest_framework import serializers
from .models import Estado


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estado
        fields='__all__'
    
    def create(self,validated_data):
            return Estado.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idestado = validated_data.get('idestado', instance.idestado)
        instance.estado = validated_data.get('estado', instance.estado)
        
        instance.save()
        return instance
