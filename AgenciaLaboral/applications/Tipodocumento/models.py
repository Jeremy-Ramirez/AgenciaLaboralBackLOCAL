from django.db import models

# Create your models here.


class Tipodocumento(models.Model):
    idtipodocumento = models.IntegerField(db_column='idtipoDocumento', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, unique=True, null=True)

    def __str__(self):
        txt = "{0}"
        return txt.format( self.descripcion)
        
    class Meta:
        verbose_name='Tipodocumento'
        verbose_name_plural='Tipodocumentos'
        db_table = 'tipodocumento'

        
        def __str__(self):
            return self.descripcion
        
