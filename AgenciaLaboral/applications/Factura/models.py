from django.db import models

# Create your models here.
from applications.Empresa.models import Empresa
from applications.Estado.models import Estado
from applications.Formapago.models import Formapago

class Factura(models.Model):
    idfactura = models.IntegerField(db_column='idFactura', primary_key=True)  # Field name made lowercase.
    numfactura = models.CharField(db_column='numFactura', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    fechaemision = models.DateTimeField(db_column='fechaEmision', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    iva = models.FloatField(db_column='IVA', blank=True, null=True)  # Field name made lowercase.
    ivatotal = models.FloatField(db_column='IVAtotal', blank=True, null=True)  # Field name made lowercase.
    codigotransaccion = models.CharField(db_column='codigoTransaccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    formapago_idformapago = models.ForeignKey(Formapago, models.DO_NOTHING, db_column='FormaPago_idFormaPago')  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='Estado_idEstado')  # Field name made lowercase.

    class Meta:
        
        db_table = 'factura'