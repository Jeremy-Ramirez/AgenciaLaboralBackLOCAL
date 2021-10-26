from django.db import models

from applications.Aspirante.models import Aspirante
from applications.Usuario.models import Usuario
from applications.CategoriaDocumento.models import CategoriaDocumento

def nameFile(instance, filename):
    return '/'.join(['archivosAspirantes', str(instance.categoriaDocumento_idcategoriadocumento.descripcion), filename])
# Create your models here.


class ArchivosAspirante(models.Model):
    idarchivosaspirante = models.AutoField(db_column='idArchivosAspirante', primary_key=True)  # Field name made lowercase.
    nombredocumento = models.CharField(db_column='nombreDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    categoriaDocumento_idcategoriadocumento = models.ForeignKey(CategoriaDocumento, models.DO_NOTHING, db_column='CategoriaDocumento_idCategoriaDocumento')  # Field name made lowercase.
    archivo = models.FileField(blank=True, upload_to=nameFile, null=True)  # Field name made lowercase.
    fechacreacion = models.DateField(db_column='fechaCreacion', blank=True, null=True)  # Field name made lowercase.
    aspirante_idaspirante = models.ForeignKey(Aspirante, models.DO_NOTHING, db_column='aspirante_idaspirante')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_idusuario',null=True) # Field name made lowercase.
    
    def __str__(self):
        txt = " id: {0} / NombreDocumento: {1} "
        return txt.format(self.idaspirante , self.nombredocumento ) 

    class Meta:
        
        db_table = 'archivosaspirante'