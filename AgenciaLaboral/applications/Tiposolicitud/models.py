from django.db import models

# Create your models here.
class Tiposolicitud(models.Model):
    idtiposolicitud = models.IntegerField(db_column='idTipoSolicitud', primary_key=True)  # Field name made lowercase.
    descrpcion = models.CharField(max_length=45, blank=True, null=True)
    
    def __str__(self):
        txt = "{0}"
        return txt.format( self.descrpcion)
    class Meta:
        verbose_name='Tiposolicitud'
        verbose_name_plural='Tiposolicituds'
        db_table = 'tiposolicitud'
        
        def __str__(self):
            return self.descrpcion