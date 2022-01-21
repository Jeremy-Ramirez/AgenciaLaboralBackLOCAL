from django.db import models


class DuracionPaquetes(models.Model):
    idduracionpaquetes = models.AutoField(db_column='idDuracionPaquetes', primary_key=True)  # Field name made lowercase.
    duracion = models.DurationField(blank=True, null=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        txt = " id: {0} / Duracion: {1} "
        return txt.format(self.idduracionpaquetes , self.duracion ) 

    class Meta:
        
        db_table = 'duracionpaquetes'
