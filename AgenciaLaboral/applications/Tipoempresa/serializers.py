from rest_framework import serializers
from .models import Tipoempresa


class TipoempresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tipoempresa
        fields='__all__'
    
    def create(self,validated_data):
            return Tipoempresa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idtipoempresa = validated_data.get('idtipoempresa', instance.idtipoempresa)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance