from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empresa
        fields= '__all__'
        #depth = 1

    '''def __init__(self, *args, **kwargs):
        super(EmpresaSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
    '''
    def create(self,validated_data):
            return Empresa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idempresa = validated_data.get('idempresa', instance.idempresa)
        instance.ruc_cedula = validated_data.get('ruc_cedula', instance.ruc_cedula)
        instance.nombrecomercial = validated_data.get('nombrecomercial', instance.nombrecomercial)
        instance.razonsocial = validated_data.get('razonsocial', instance.razonsocial)
        instance.calleprincipal = validated_data.get('calleprincipal', instance.calleprincipal)
        instance.callesecundaria = validated_data.get('callesecundaria', instance.callesecundaria)
        instance.mz = validated_data.get('mz', instance.mz)
        instance.villa = validated_data.get('villa', instance.villa)
        instance.referencia = validated_data.get('referencia', instance.referencia)
        instance.telefonooficina = validated_data.get('telefonooficina', instance.telefonooficina)
        instance.celular = validated_data.get('celular', instance.celular)
        instance.correoelectronico = validated_data.get('correoelectronico', instance.correoelectronico)
        instance.contrasenia = validated_data.get('contrasenia', instance.contrasenia)
        instance.paginaweb = validated_data.get('paginaweb', instance.paginaweb)
        instance.tipodocumento_idtipodocumento = validated_data.get('tipodocumento_idtipodocumento', instance.tipodocumento_idtipodocumento)
        instance.tipopersona_idtipopersona = validated_data.get('tipopersona_idtipopersona', instance.tipopersona_idtipopersona)
        instance.actividadeconomica_idactividadeconomica = validated_data.get('actividadeconomica_idactividadeconomica', instance.actividadeconomica_idactividadeconomica)
        instance.ramaactividad_idramaactividad = validated_data.get('ramaactividad_idramaactividad', instance.ramaactividad_idramaactividad)
        instance.sector_idsector = validated_data.get('sector_idsector', instance.sector_idsector)
        instance.tipoempresa_idtipoempresa = validated_data.get('tipoempresa_idtipoempresa', instance.tipoempresa_idtipoempresa)
        instance.provincia_idprovincia = validated_data.get('provincia_idprovincia', instance.provincia_idprovincia)
        instance.ciudad_idciudad = validated_data.get('ciudad_idciudad', instance.ciudad_idciudad)


        instance.save()
        return instance
