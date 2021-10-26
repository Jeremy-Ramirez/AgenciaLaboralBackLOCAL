from django.db import models

# Create your models here.



class Estado(models.Model):
    idestado = models.AutoField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        txt = "{0}"
        return txt.format(self.estado)
    
    class Meta:
        verbose_name='Estado'
        verbose_name_plural='Estados'
        db_table = 'estado'
        
        def __str__(self):
            return self.estado