from rest_framework import serializers
from .models import Tiposolicitud


class TiposolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tiposolicitud
        fields='__all__'
    
    
    def create(self,validated_data):
            return Tiposolicitud.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idtiposolicitud = validated_data.get('idtiposolicitud', instance.idtiposolicitud)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance