from django.db import models

# Create your models here.



class EstadoAspirantes(models.Model):
    idestadoaspirantes = models.AutoField(db_column='idEstadoAspirantes', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        txt = "{0}"
        return txt.format(self.estado)
    
    class Meta:
        verbose_name='EstadoAspirantes'
        verbose_name_plural='EstadoAspirantes'
        db_table = 'estadoaspirantes'
        
        def __str__(self):
            return self.estado
