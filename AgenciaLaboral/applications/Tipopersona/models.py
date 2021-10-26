from django.db import models

# Create your models here.

class Tipopersona(models.Model):
    idtipopersona = models.IntegerField(db_column='idtipoPersona', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, unique=True, null=True)
    
    def __str__(self):
        txt = "{0}"
        return txt.format( self.descripcion)

    class Meta:
        verbose_name='Tipopersona'
        verbose_name_plural='Tipopersonas'
        db_table = 'tipopersona'

        def __str__(self):
            return self.descripcion