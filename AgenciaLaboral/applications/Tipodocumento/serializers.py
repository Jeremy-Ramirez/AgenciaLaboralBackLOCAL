
from rest_framework import serializers
from .models import Tipodocumento

class TipodocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tipodocumento
        fields='__all__'

    def create(self,validated_data):
            return Tipodocumento.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idtipodocumento = validated_data.get('idtipodocumento', instance.idtipodocumento)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance
