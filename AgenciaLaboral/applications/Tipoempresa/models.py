from django.db import models

# Create your models here.

class Tipoempresa(models.Model):
    idtipoempresa = models.AutoField(db_column='idtipoEmpresa', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, unique=True, null=True)
    
    def __str__(self):
        txt = "{0}"
        return txt.format( self.descripcion)        

    class Meta:
        verbose_name='Tipoempresa'
        verbose_name_plural='Tipoempresas'
        db_table = 'tipoempresa'

        
        def __str__(self):
            return self.descripcion
        