from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import Aspirante
from rest_framework.views import APIView

class AspiranteSerializer(serializers.ModelSerializer):

    class Meta:
        model=Aspirante
        fields='__all__'

    def create(self,validated_data):
        return Aspirante.objects.create(**validated_data)



    def update(self, instance, validated_data):
        instance.idaspirante = validated_data.get('idaspirante',instance.idaspirante)
        instance.numerohijos = validated_data.get('numerohijos',instance.numerohijos)
        instance.salarioMinimoAceptado = validated_data.get('salarioMinimoAceptado',instance.salarioMinimoAceptado)
        instance.descripcionPerfilProfesional = validated_data.get('descripcionPerfilProfesional',instance.descripcionPerfilProfesional)
        instance.videopresentacion = validated_data.get('videopresentacion',instance.videopresentacion)
        instance.aniosexperiencia = validated_data.get('aniosexperiencia',instance.aniosexperiencia)
        instance.fechanacimiento = validated_data.get('fechanacimiento',instance.fechanacimiento)
        instance.posibilidadviajar = validated_data.get('posibilidadviajar',instance.posibilidadviajar)
        instance.posibilidadcambioresidencia = validated_data.get('posibilidadcambioresidencia',instance.posibilidadcambioresidencia)
        instance.profesiones_idprofesiones = validated_data.get('profesiones_idprofesiones',instance.profesiones_idprofesiones)
        instance.idiomas = validated_data.get('idiomas',instance.idiomas)
        instance.usuario_idusuario = validated_data.get('usuario_idusuario',instance.usuario_idusuario)
        instance.estadoaspirantes_idestadoaspirantes = validated_data.get('estadoaspirantes_idestadoaspirantes',instance.estadoaspirantes_idestadoaspirantes)

        
        instance.save()
        return instance