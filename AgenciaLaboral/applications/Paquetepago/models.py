from django.db import models

from applications.Estado.models import Estado
from applications.Usuario.models import Usuario

# Create your models here.

class Paquetepago(models.Model):
    idpaquetepago = models.IntegerField(db_column='idPaquetePago', primary_key=True)  # Field name made lowercase.
    nombrepaquete = models.CharField(db_column='nombrePaquete', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    duracion = models.TimeField(blank=True, null=True)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    fechacaducidad = models.DateTimeField(db_column='fechaCaducidad', blank=True, null=True)  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='Estado_idEstado')  # Field name made lowercase.

    class Meta:
        
        db_table = 'paquetepago'