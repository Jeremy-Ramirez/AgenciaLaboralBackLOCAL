from django.db import models

# Create your models here.


from applications.Usuario.models import Usuario

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.titulo), filename])

class Sugerencia(models.Model):
    idsugerencia = models.AutoField(db_column='idSugerencia', primary_key=True)  # Field name made lowercase.    titulo = models.CharField(max_length=45, blank=True, null=True)
    titulo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=450, blank=True, null=True)
    imagen = models.ImageField(blank=True, upload_to=nameFile, null=True)
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        
        db_table = 'sugerencia'