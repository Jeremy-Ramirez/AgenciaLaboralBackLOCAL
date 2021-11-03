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
        instance.experiencialaboral = validated_data.get('experiencialaboral',instance.experiencialaboral)
        instance.campolaboral = validated_data.get('campolaboral',instance.campolaboral)
        instance.experticia = validated_data.get('experticia',instance.experticia)
        instance.videopresentacion = validated_data.get('videopresentacion',instance.videopresentacion)
        instance.aniosexperiencia = validated_data.get('aniosexperiencia',instance.aniosexperiencia)
        instance.fechanacimiento = validated_data.get('fechanacimiento',instance.fechanacimiento)
        instance.posibilidadviajar = validated_data.get('posibilidadviajar',instance.posibilidadviajar)
        instance.profesiones_idprofesiones = validated_data.get('profesiones_idprofesiones',instance.profesiones_idprofesiones)
        instance.usuario_idusuario = validated_data.get('usuario_idusuario',instance.usuario_idusuario)
        
        instance.save()
        return instance