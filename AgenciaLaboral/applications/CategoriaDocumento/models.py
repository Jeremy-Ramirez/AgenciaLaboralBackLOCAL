from django.db import models

# Create your models here.


class CategoriaDocumento(models.Model):
    idcategoriadocumento = models.AutoField(db_column='idCategoriaDocumento', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, unique=True, null=True)

    def __str__(self):
        txt = "{0}"
        return txt.format( self.descripcion)
        
    class Meta:
        verbose_name='Categoriadocumento'
        verbose_name_plural='Categoriadocumento'
        db_table = 'categoriadocumento'

        
        def __str__(self):
            return self.descripcion