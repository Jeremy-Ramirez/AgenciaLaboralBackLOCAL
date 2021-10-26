from rest_framework import serializers
from .models import Provincia


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Provincia
        fields='__all__'
    
    def create(self,validated_data):
            return Provincia.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idprovincia = validated_data.get('idprovincia', instance.idprovincia)
        instance.nombreprovincia = validated_data.get('nombreprovincia', instance.nombreprovincia)
        
        instance.save()
        return instance
