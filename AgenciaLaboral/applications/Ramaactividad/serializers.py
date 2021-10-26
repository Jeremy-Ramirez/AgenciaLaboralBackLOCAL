from rest_framework import serializers
from .models import Ramaactividad


class RamaactividadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ramaactividad
        fields='__all__'
    
    
    def create(self,validated_data):
            return Ramaactividad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idramaactividad = validated_data.get('idramaactividad', instance.idramaactividad)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance