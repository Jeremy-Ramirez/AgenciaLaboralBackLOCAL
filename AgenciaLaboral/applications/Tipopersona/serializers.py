from rest_framework import serializers
from .models import Tipopersona


class TipopersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tipopersona
        fields='__all__'
    
    
    def create(self,validated_data):
            return Tipopersona.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idtipopersona = validated_data.get('idtipopersona', instance.idtipopersona)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance