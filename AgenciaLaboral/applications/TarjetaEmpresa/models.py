from django.db import models

# Create your models here.
from applications.Empresa.models import Empresa

class TarjetaEmpresa(models.Model):
    idtarjeta_empresa = models.IntegerField(db_column='idTarjeta-Empresa', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numerotarjeta = models.CharField(db_column='numeroTarjeta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tiptarjeta = models.CharField(db_column='tipTarjeta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.

    class Meta:
      
        db_table = 'tarjeta-empresa'
