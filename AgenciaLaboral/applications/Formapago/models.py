from django.db import models

# Create your models here.

class Formapago(models.Model):
    idformapago = models.IntegerField(db_column='idFormaPago', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        
        db_table = 'formapago'