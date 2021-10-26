from rest_framework import serializers
from .models import Solicitud


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model=Solicitud
        fields='__all__'
        depth = 2
    
    
    def create(self,validated_data):
            return Solicitud.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idsolicitud = validated_data.get('idsolicitud', instance.idsolicitud)
        instance.profesion = validated_data.get('profesion', instance.profesion)
        instance.aniosexperiencia = validated_data.get('aniosexperiencia', instance.aniosexperiencia)
        instance.rangoedad = validated_data.get('rangoedad', instance.rangoedad)
        instance.experticia = validated_data.get('experticia', instance.experticia)
        instance.sueldo = validated_data.get('sueldo', instance.sueldo)
        instance.fechainicio = validated_data.get('fechainicio', instance.fechainicio)
        instance.fechacierre = validated_data.get('fechacierre', instance.fechacierre)
        instance.cargo = validated_data.get('cargo', instance.cargo)
        instance.descripcioncargo = validated_data.get('descripcioncargo', instance.descripcioncargo)
        instance.tiposolicitud_idtiposolicitud = validated_data.get('tiposolicitud_idtiposolicitud', instance.tiposolicitud_idtiposolicitud)
        instance.estado_idestado = validated_data.get('estado_idestado', instance.estado_idestado)
        instance.representante_idrepresentante = validated_data.get('representante_idrepresentante', instance.representante_idrepresentante)
        instance.provincia_idprovincia = validated_data.get('provincia_idprovincia', instance.provincia_idprovincia)
        instance.ciudad_idciudad = validated_data.get('ciudad_idciudad', instance.ciudad_idciudad)
        
        instance.save()
        return instance