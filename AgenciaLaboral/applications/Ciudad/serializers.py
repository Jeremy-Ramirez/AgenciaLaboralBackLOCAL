from rest_framework import serializers
from .models import Ciudad


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ciudad
        fields='__all__'
    
    
    def create(self,validated_data):
            return Ciudad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idciudad = validated_data.get('idciudad', instance.idciudad)
        instance.nombreciudad = validated_data.get('nombreciudad', instance.nombreciudad)
        instance.provincia_idprovincia = validated_data.get('provincia_idprovincia', instance.provincia_idprovincia)

        instance.save()
        return instance
