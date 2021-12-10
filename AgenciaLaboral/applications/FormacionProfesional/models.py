from django.db import models

from applications.Aspirante.models import Aspirante
from applications.Aspirante.models import NivelEstudios
#def nameFile(instance, filename):
#    return '/'.join(['archivosAspirantes', str(instance.categoriaDocumento_idcategoriadocumento.descripcion), filename])
# Create your models here.


class FormacionProfesional(models.Model):
    idformacionprofesional = models.AutoField(db_column='idFormacionProfesional', primary_key=True)  # Field name made lowercase.
    nivelestudios_idnivelestudios = models.ForeignKey(NivelEstudios, models.DO_NOTHING, db_column='NivelEstudios_idNivelEstudios', null=True)  # Field name made lowercase.    centroeducativo = models.CharField(db_column='centroEducativo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    centroeducativo = models.CharField(db_column='centroEducativo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    areaestudios = models.CharField(db_column='areaEstudios', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estadoestudios = models.CharField(max_length=50,db_column='estadoEstudios', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.DateField(db_column='fechaCierre', blank=True, null=True)  # Field name made lowercase.
    aspirante_idaspirante = models.ForeignKey(Aspirante, models.DO_NOTHING, db_column='aspirante_idaspirante')  # Field name made lowercase.
    
    def __str__(self):
        txt = " id: {0}"
        return txt.format(self.idformacionprofesional) 

    class Meta:
        
        db_table = 'formacionprofesional'