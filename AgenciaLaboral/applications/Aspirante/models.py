from django.db import models

from applications.Profesiones.models import Profesiones
from applications.Usuario.models import Usuario

def nameFile(instance, filename):
    return '/'.join(['videos', str(instance.profesiones_idprofesiones.profesion), filename])
# Create your models here.
class Aspirante(models.Model):
    idaspirante = models.AutoField(db_column='idAspirante', primary_key=True)  # Field name made lowercase.
    numerohijos = models.IntegerField(db_column='numeroHijos', blank=True, null=True)  # Field name made lowercase.
    experiencialaboral = models.CharField(db_column='experienciaLaboral', max_length=45, blank=True, null=True)  # Field name made lowercase.
    campolaboral = models.CharField(db_column='campoLaboral', max_length=45, blank=True, null=True)  # Field name made lowercase.
    experticia = models.CharField(max_length=45, blank=True, null=True)
    videopresentacion = models.FileField(blank=True, upload_to=nameFile, null=True)  # Field name made lowercase.
    aniosexperiencia = models.IntegerField(db_column='aniosExperiencia', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    posibilidadviajar = models.IntegerField(db_column='posibilidadViajar', blank=True, null=True)  # Field name made lowercase.
    profesiones_idprofesiones = models.ForeignKey(Profesiones, models.DO_NOTHING, db_column='Profesiones_idProfesiones')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_idusuario',null=True) # Field name made lowercase.
    
    def __str__(self):
        txt = " id: {0} / Experiencia: {1} / Campo: {2} "
        return txt.format(self.idaspirante , self.experiencialaboral , self.campolaboral ) 

    class Meta:
        
        db_table = 'aspirante'