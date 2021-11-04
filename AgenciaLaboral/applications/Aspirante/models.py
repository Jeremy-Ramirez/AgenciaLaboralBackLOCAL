from django.db import models

from applications.Profesiones.models import Profesiones
from applications.Usuario.models import Usuario
from applications.NivelEstudios.models import NivelEstudios

def nameFile(instance, filename):
    return '/'.join(['videos', str(instance.profesiones_idprofesiones.profesion), filename])
# Create your models here.
class Aspirante(models.Model):
    idaspirante = models.AutoField(db_column='idAspirante', primary_key=True)  # Field name made lowercase.
    numerohijos = models.IntegerField(db_column='numeroHijos', blank=True, null=True)  # Field name made lowercase.
    experiencialaboral = models.CharField(db_column='experienciaLaboral', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campolaboral = models.CharField(db_column='campoLaboral', max_length=100, blank=True, null=True)  # Field name made lowercase.
    experticia = models.CharField(max_length=800, blank=True, null=True)
    videopresentacion = models.FileField(blank=True, upload_to=nameFile, null=True)  # Field name made lowercase.
    aniosexperiencia = models.IntegerField(db_column='aniosExperiencia', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    posibilidadviajar = models.CharField(max_length=5,db_column='posibilidadViajar', blank=True, null=True)  # Field name made lowercase.
    posibilidadcambioresidencia = models.CharField(max_length=5,db_column='posibilidadCambioResidencia', blank=True, null=True)  # Field name made lowercase.
    estadoestudios = models.CharField(max_length=50,db_column='estadoEstudios', blank=True, null=True)  # Field name made lowercase.
    profesiones_idprofesiones = models.ForeignKey(Profesiones, models.DO_NOTHING, db_column='Profesiones_idProfesiones', null=True)  # Field name made lowercase.
    idiomas = models.CharField(max_length=500,db_column='idiomas', blank=True, null=True)  # Field name made lowercase.
    nivelestudios_idnivelestudios = models.ForeignKey(NivelEstudios, models.DO_NOTHING, db_column='NivelEstudios_idNivelEstudios', null=True)  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_idusuario',null=True) # Field name made lowercase.
    
    def __str__(self):
        txt = " id: {0} / Experiencia: {1} / Campo: {2} "
        return txt.format(self.idaspirante , self.experiencialaboral , self.campolaboral ) 

    class Meta:
        
        db_table = 'aspirante'