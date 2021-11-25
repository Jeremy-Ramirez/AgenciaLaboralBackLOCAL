
from rest_framework import serializers
#from django.contrib.auth.models import Usuario
from .models import Usuario
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
#from rest_framework.generics import CreateAPIView
from passlib.hash import pbkdf2_sha256

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model=Usuario
        fields='__all__'
        extra_kwargs = {
            'contrasenia': {'write_only': True}
        }
        
    def create(self,validated_data):
        '''instance = Usuario.objects.create(**validated_data)
        instance.contrasenia=pbkdf2_sha256.hash(validated_data['contrasenia'])
        instance.save()
        return instance'''
        
        return Usuario.objects.create(**validated_data)
        '''fields=('idusuario', 'nombreusuario', 'correo', 'contrasenia')
        extra_kwargs={
            'contrasenia': {'write_only': True}
        }'''

    '''#hash la password
    def create(self,validated_data):
        contrasenia=validated_data.pop('contrasenia',None)
        #instance= self.Meta.model(**validated_data)
        instance=Usuario.objects.create(**validated_data)
        if contrasenia is not None:
            instance.set_password(contrasenia)
        instance.save()
        return instance
        Usuario.objects.create(**validated_data)'''

  

    #idusuario = serializers.ReadOnlyField()
    #nombreusuario = serializers.CharField()  # Field name made lowercase.
    #contrasenia = serializers.CharField()
    #cedula = serializers.CharField()
    #nombre = serializers.CharField()
    #apellido = serializers.CharField()
    #correo = serializers.CharField()
    #telefono = serializers.CharField()
    #direccion = serializers.CharField()
    #estadocuenta = serializers.CharField()  # Field name made lowercase.
    #genero_idgenero = serializers.CharField()  # Field name made lowercase.
    #rol_idrol = serializers.CharField()  # Field name made lowercase.
    #estadocivil_idestadocivil = serializers.CharField()  # Field name made lowercase.
    #provincia_idprovincia = serializers.CharField()  # Field name made lowercase.
    #ciudad_idciudad = serializers.CharField()  # Field name made lowercase.

    

    

    def update(self, instance, validated_data):
        instance.idusuario = validated_data.get('idusuario',instance.idusuario)
        instance.nombreusuario = validated_data.get('nombreusuario',instance.nombreusuario)
        instance.contrasenia = validated_data.get('contrasenia',instance.contrasenia)
        #instance.tipodocumento_idtipodocumento = validated_data.get('tipodocumento_idtipodocumento',instance.tipodocumento_idtipodocumento)
        #instance.nodocumento = validated_data.get('nodocumento',instance.nodocumento)
        #instance.nombre = validated_data.get('nombre',instance.nombre)
        #instance.apellido = validated_data.get('apellido',instance.apellido)
        #instance.correo = validated_data.get('correo',instance.correo)
        instance.telefono = validated_data.get('telefono',instance.telefono)
        instance.direccion = validated_data.get('direccion',instance.direccion)
        instance.estado_idestado = validated_data.get('estado_idestado',instance.estado_idestado)
        instance.genero_idgenero =validated_data.get('genero_idgenero',instance.genero_idgenero)  # Field name made lowercase.
        instance.rol_idrol = validated_data.get('rol_idrol',instance.rol_idrol) # Field name made lowercase.
        instance.estadocivil_idestadocivil = validated_data.get('estadocivil_idestadocivil',instance.estadocivil_idestadocivil) # Field name made lowercase.
        instance.provincia_idprovincia = validated_data.get('provincia_idprovincia',instance.provincia_idprovincia)# Field name made lowercase.
        instance.ciudad_idciudad =validated_data.get('ciudad_idciudad',instance.ciudad_idciudad) # Field name made lowercase.
        instance.save()
        return instance