from rest_framework import serializers
from .models import Estadocivil


class EstadocivilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estadocivil
        fields='__all__'
    
    def create(self,validated_data):
            return Estadocivil.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idestadocivil = validated_data.get('idestadocivil', instance.idestadocivil)
        instance.estadocivil = validated_data.get('estadocivil', instance.estadocivil)
        
        instance.save()
        return instance
