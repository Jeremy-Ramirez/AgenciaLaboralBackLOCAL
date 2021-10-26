from django.db import models
from applications.Genero.models import Genero
from applications.Rol.models import Rol
from applications.Ciudad.models import Ciudad
from applications.Tipodocumento.models import Tipodocumento
from applications.Estadocivil.models import Estadocivil
from applications.Provincia.models import Provincia
from applications.Estado.models import Estado

class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idusuario', primary_key=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contrasenia = models.CharField(max_length=150, blank=True, null=True)
    tipodocumento_idtipodocumento = models.ForeignKey(Tipodocumento, models.DO_NOTHING, db_column='tipodocumento_idtipodocumento',null=True)  # Field name made lowercase.
    nodocumento = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True, unique=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estadoCuenta', null=True)   # Field name made lowercase.
    genero_idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='Genero_idGenero', null=True)  # Field name made lowercase.
    rol_idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='Rol_idRol')  # Field name made lowercase.
    estadocivil_idestadocivil = models.ForeignKey(Estadocivil, models.DO_NOTHING, db_column='EstadoCivil_idEstadoCivil', null=True)  # Field name made lowercase.
    provincia_idprovincia = models.ForeignKey(Provincia, models.DO_NOTHING, db_column='Provincia_idProvincia', null=True)  # Field name made lowercase.
    ciudad_idciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='Ciudad_idCiudad', null=True)  # Field name made lowercase.


    def __str__(self):
        txt = " No.documento: {0} / Nombres: {1} {2} / Correo: {3} / Teléfono: {4} / Dirección: {5}"
        return txt.format(self.nodocumento , self.nombre , self.apellido , self.correo , self.telefono, self.direccion) 

    def getById(self, idusuario):
        try:
            usuario = Usuario.objects.get(idusuario=idusuario)
            return usuario
        except:
            return None


    USERNAME_FIELD='correo'
    REQUIRED_FIELDS=[]

    

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table = 'usuario'

        def __str__(self):
            txt = " No.documento: {0} / Nombres: {1} {2} / Correo: {3} / Teléfono: {4} / Dirección: {5}"
            return txt.format(self.nodocumento , self.nombre , self.apellido , self.correo , self.telefono, self.direccion) 

