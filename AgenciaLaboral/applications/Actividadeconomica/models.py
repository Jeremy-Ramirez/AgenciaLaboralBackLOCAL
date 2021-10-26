from django.db import models

# Create your models here.


class Actividadeconomica(models.Model):
    idactividadeconomica = models.AutoField(db_column='idactividadEconomica', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, unique=True, null=True)
    
    def __str__(self):
        txt = "{0}"
        return txt.format( self.descripcion)
        
    class Meta:
        verbose_name='Actividadeconomica'
        verbose_name_plural='Actividadeconomicas'
        db_table = 'actividadeconomica'

        def __str__(self):
            return self.descripcion