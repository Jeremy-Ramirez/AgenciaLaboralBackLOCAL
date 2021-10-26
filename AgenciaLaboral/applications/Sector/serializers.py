from rest_framework import serializers
from .models import Sector


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sector
        fields='__all__'
    
    
    def create(self,validated_data):
            return Sector.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idsector = validated_data.get('idsector', instance.idsector)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance