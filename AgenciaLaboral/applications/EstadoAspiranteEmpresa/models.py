from django.db import models

# Create your models here.



class EstadoAspiranteEmpresa(models.Model):
    idestadoaspiranteempresa = models.AutoField(db_column='idEstadoAspiranteEmpresa', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        txt = "{0}"
        return txt.format(self.estado)
    
    class Meta:
        verbose_name='EstadoAspiranteEmpresa'
        verbose_name_plural='EstadoAspiranteEmpresa'
        db_table = 'EstadoAspiranteEmpresa'
        
        def __str__(self):
            return self.estado