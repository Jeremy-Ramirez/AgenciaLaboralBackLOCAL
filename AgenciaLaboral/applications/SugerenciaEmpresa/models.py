from django.db import models

# Create your models here.


from applications.Empresa.models import Empresa

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.titulo), filename])

class SugerenciaEmpresa(models.Model):
    idsugerenciaempresa = models.AutoField(db_column='idSugerenciaEmpresa', primary_key=True)  # Field name made lowercase.    titulo = models.CharField(max_length=45, blank=True, null=True)
    titulo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=450, blank=True, null=True)
    imagen = models.ImageField(blank=True, upload_to=nameFile, null=True)
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.

    class Meta:
        
        db_table = 'sugerenciaEmpresa'