from django.db import models

# Create your models here.



class Sector(models.Model):
    idsector = models.AutoField(db_column='idSector', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, unique=True, null=True)
    
    def __str__(self):
        txt = "{0}"
        return txt.format( self.descripcion)

    class Meta:
        verbose_name='Sector'
        verbose_name_plural='Sectores'
        db_table = 'sector'
        def __str__(self):
            return self.descripcion