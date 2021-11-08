from django.db import models
from applications.Tiposolicitud.models import Tiposolicitud
from applications.Estado.models import Estado
from applications.Ciudad.models import Ciudad
from applications.Profesiones.models import Profesiones
from applications.Representanteempresa.models import Representanteempresa
from applications.Provincia.models import Provincia
from applications.NivelEstudios.models import NivelEstudios
#falta ciudad, provincia, idempresa, idusuario
class Solicitud(models.Model):
    idsolicitud = models.AutoField(db_column='idSolicitud', primary_key=True)  # Field name made lowercase.
    profesiones_idprofesiones = models.ForeignKey(Profesiones, models.DO_NOTHING, db_column='Profesiones_idProfesiones', null=True)  # Field name made lowercase.
    aniosexperiencia = models.IntegerField(db_column='aniosExperiencia', blank=True, null=True)  # Field name made lowercase.
    rangoedad = models.CharField(db_column='rangoEdad', max_length=45, blank=True, null=True)  # Field name made lowercase.
    experticia = models.CharField(max_length=45, blank=True, null=True)
    sueldo = models.FloatField(blank=True, null=True)
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.DateField(db_column='fechaCierre', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(max_length=100, blank=True, null=True)
    descripcioncargo = models.TextField(db_column='descripcionCargo', blank=True, null=True)  
    tiposolicitud_idtiposolicitud = models.ForeignKey(Tiposolicitud, models.DO_NOTHING, db_column='TipoSolicitud_idTipoSolicitud', null = True)  # Field name made lowercase.
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='Estado_idEstado', null = True)  # Field name made lowercase.
    representante_idrepresentante = models.ForeignKey(Representanteempresa, models.DO_NOTHING, db_column='representante_idrepresentante' , null = True)  # Field name made lowercase.
    provincia_idprovincia = models.ForeignKey(Provincia, models.DO_NOTHING, db_column='provincia_idProvincia', null=True)  # Field name made lowercase.
    ciudad_idciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_idCiudad', null=True)  # Field name made lowercase.
    nivelestudios_idnivelestudios = models.ForeignKey(NivelEstudios, models.DO_NOTHING, db_column='NivelEstudios_idNivelEstudios', null=True)  # Field name made lowercase.
    jornada = models.CharField(max_length=45, blank=True, null=True)
    discapacidad = models.CharField(max_length=45, blank=True, null=True)
    posibilidadviajar = models.CharField(max_length=5,db_column='posibilidadViajar', blank=True, null=True)  # Field name made lowercase.
    posibilidadcambioresidencia = models.CharField(max_length=5,db_column='posibilidadCambioResidencia', blank=True, null=True)  # Field name made lowercase.
    licencia =   models.CharField(max_length=45, blank=True, null=True)    
    idiomas =   models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        txt = "Cargo: {0} "
        return txt.format(self.cargo) 

    class Meta:
        verbose_name='Solicitud'
        verbose_name_plural='Solicituds'
        db_table = 'solicitud'

        def __str__(self):
            txt = "Cargo: {0} "
            return txt.format(self.cargo) 
        