from django.db import models

# Create your models here.
from applications.Empresa.models import Empresa
from applications.Usuario.models import Usuario

class Representanteempresa(models.Model):
    idrepresentanteempresa = models.AutoField(db_column='idRepresentanteEmpresa', primary_key=True)  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        
        db_table = 'representanteempresa'