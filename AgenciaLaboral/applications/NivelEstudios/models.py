from django.db import models

# Create your models here.


class NivelEstudios(models.Model):
    idnivelestudios = models.AutoField(db_column='idNivelEstudios', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, unique=True, null=True)

    def __str__(self):
        txt = "{0}"
        return txt.format( self.descripcion)
        
    class Meta:
        verbose_name='nivelEstudios'
        verbose_name_plural='nivelEstudios'
        db_table = 'nivelEstudion'

        
        def __str__(self):
            return self.descripcion