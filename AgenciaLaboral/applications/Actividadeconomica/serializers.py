from rest_framework import serializers
from .models import Actividadeconomica


class ActividadeconomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actividadeconomica
        fields='__all__'
    
    def create(self,validated_data):
            return Actividadeconomica.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idactividadeconomica = validated_data.get('idactividadeconomica', instance.idactividadeconomica)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance