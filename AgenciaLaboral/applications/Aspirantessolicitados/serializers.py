from rest_framework import serializers
from .models import Aspirantessolicitados 

class AspirantessolicitadosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aspirantessolicitados
        fields= '__all__'
        #depth = 3
    
    def create(self,validated_data):
            return Aspirantessolicitados.objects.create(**validated_data)
     
    def update(self, instance, validated_data):
        instance.idaspirantessolicitados = validated_data.get('idaspirantessolicitados', instance.idaspirantessolicitados)
        instance.fechaaceptacion = validated_data.get('fechaaceptacion', instance.fechaaceptacion)
        instance.solicitud_idsolicitud = validated_data.get('solicitud_idsolicitud', instance.solicitud_idsolicitud)
        instance.estado_idestado = validated_data.get('estado_idestado', instance.estado_idestado)
        instance.aspirante_idaspirante = validated_data.get('aspirante_idaspirante', instance.aspirante_idaspirante)


        instance.save()
        return instance
