from django.db import models

from applications.Estado.models import Estado
from applications.Usuario.models import Usuario
from applications.DuracionPaquetes.models import DuracionPaquetes
# Create your models here.

class Paquetepago(models.Model):
    idpaquetepago = models.AutoField(db_column='idPaquetePago', primary_key=True)  # Field name made lowercase.
    nombrepaquete = models.CharField(db_column='nombrePaquete', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    duracionpaquetes_idduracionpaquetes = models.ForeignKey(DuracionPaquetes, models.DO_NOTHING, db_column='DuracionPaquetes_idDuracionPaquetes',null=True)  # Field name made lowercase.
    fecharegistro = models.DateField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    fechacaducidad = models.DateField(db_column='fechaCaducidad', blank=True, null=True)  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='Estado_idEstado')  # Field name made lowercase.

    class Meta:
        
        db_table = 'paquetepago'