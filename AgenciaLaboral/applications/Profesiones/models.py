from django.db import models

# Create your models here.


class Profesiones(models.Model):
    idprofesiones = models.AutoField(db_column='idProfesiones', primary_key=True)  # Field name made lowercase.
    profesion = models.CharField(max_length=45, blank=True, null=True)


    def __str__(self):
        txt = " id: {0} / profesion: {1} "
        return txt.format(self.idprofesiones , self.profesion ) 

    class Meta:
        
        db_table = 'profesiones'


     