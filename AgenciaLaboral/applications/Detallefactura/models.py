from django.db import models

# Create your models here.
from applications.Factura.models import Factura
from applications.Paquetepago.models import Paquetepago

class Detallefactura(models.Model):
    paquetepago_idpaquetepago = models.OneToOneField(Paquetepago, models.DO_NOTHING, db_column='PaquetePago_idPaquetePago', primary_key=True)  # Field name made lowercase.
    factura_idfactura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='Factura_idFactura')  # Field name made lowercase.
    iddetallefactura = models.IntegerField(db_column='idDetalleFactura')  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    preciounitario = models.FloatField(db_column='precioUnitario', blank=True, null=True)  # Field name made lowercase.
    totaldetalle = models.FloatField(db_column='totalDetalle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'detallefactura'
        unique_together = (('paquetepago_idpaquetepago', 'factura_idfactura', 'iddetallefactura'),)