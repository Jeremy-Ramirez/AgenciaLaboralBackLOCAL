from django.db import models

from applications.Profesiones.models import Profesiones
from applications.Usuario.models import Usuario
from applications.NivelEstudios.models import NivelEstudios
from applications.EstadoAspirantes.models import EstadoAspirantes

def nameFile(instance, filename):
    return '/'.join(['videos', str(instance.profesiones_idprofesiones.profesion), filename])
# Create your models here.
class Aspirante(models.Model):
    idaspirante = models.AutoField(db_column='idAspirante', primary_key=True)  # Field name made lowercase.
    numerohijos = models.IntegerField(db_column='numeroHijos', blank=True, null=True)  # Field name made lowercase.
    salarioMinimoAceptado = models.IntegerField(db_column='salarioMinimoAceptado', blank=True, null=True)  # Field name made lowercase.
    descripcionPerfilProfesional = models.CharField(db_column='descripcionPerfilProfesional', max_length=100, blank=True, null=True)  # Field name made lowercase.
    videopresentacion = models.FileField(blank=True, upload_to=nameFile, null=True)  # Field name made lowercase.
    aniosexperiencia = models.IntegerField(db_column='aniosExperiencia', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    posibilidadviajar = models.CharField(max_length=5,db_column='posibilidadViajar', blank=True, null=True)  # Field name made lowercase.
    posibilidadcambioresidencia = models.CharField(max_length=5,db_column='posibilidadCambioResidencia', blank=True, null=True)  # Field name made lowercase.
    profesiones_idprofesiones = models.ForeignKey(Profesiones, models.DO_NOTHING, db_column='Profesiones_idProfesiones', null=True)  # Field name made lowercase.
    idiomas = models.CharField(max_length=500,db_column='idiomas', blank=True, null=True)  # Field name made lowercase.
    estadoaspirantes_idestadoaspirantes = models.ForeignKey(EstadoAspirantes, models.DO_NOTHING, db_column='estadoaspirantes_idestadoaspirantes',null=True) # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_idusuario',null=True) # Field name made lowercase.
    
    def __str__(self):
        txt = " id: {0} "
        return txt.format(self.idaspirante ) 

    class Meta:
        
        db_table = 'aspirante'