from django.db import models
from applications.Tipodocumento.models import Tipodocumento
from applications.Tipopersona.models  import Tipopersona
from applications.Actividadeconomica.models import Actividadeconomica
from applications.Ramaactividad.models import Ramaactividad
from applications.Sector.models import Sector
from applications.Tipoempresa.models import Tipoempresa
from applications.Ciudad.models import Ciudad
from applications.Provincia.models import Provincia
from applications.Estado.models import Estado
class Empresa(models.Model):
    idempresa = models.AutoField(db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    ruc_cedula = models.CharField(db_column='ruc/cedula', max_length=45, unique=True, null=True)  # Field renamed to remove unsuitable characters.
    nombrecomercial = models.CharField(db_column='nombreComercial', max_length=45, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='razonSocial', max_length=45, blank=True, null=True)  # Field name made lowercase.
    calleprincipal = models.CharField(db_column='callePrincipal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    callesecundaria = models.CharField(db_column='calleSecundaria', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mz = models.CharField(max_length=45, blank=True, null=True)
    villa = models.CharField(max_length=45, blank=True, null=True)
    referencia = models.CharField(max_length=45, blank=True, null=True)
    telefonooficina = models.CharField(db_column='telefonoOficina', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(db_column='correo', max_length=45, unique=True, null=True)  # Field name made lowercase.
    contrasenia = models.CharField(max_length=16, blank=True, null=True)    
    paginaweb = models.CharField(db_column='paginaWeb', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodocumento_idtipodocumento = models.ForeignKey(Tipodocumento, models.DO_NOTHING, db_column='tipoDocumento_idtipoDocumento', null = True)  # Field name made lowercase.
    tipopersona_idtipopersona = models.ForeignKey(Tipopersona, models.DO_NOTHING, db_column='tipoPersona_idtipoPersona', null = True)  # Field name made lowercase.
    actividadeconomica_idactividadeconomica = models.ForeignKey(Actividadeconomica, models.DO_NOTHING, db_column='actividadEconomica_idactividadEconomica', null = True)  # Field name made lowercase.
    ramaactividad_idramaactividad = models.ForeignKey(Ramaactividad, models.DO_NOTHING, db_column='ramaActividad_idramaActividad', null = True)  # Field name made lowercase.
    sector_idsector = models.ForeignKey(Sector, models.DO_NOTHING, db_column='sector_idSector', null = True)  # Field name made lowercase.
    tipoempresa_idtipoempresa = models.ForeignKey(Tipoempresa, models.DO_NOTHING, db_column='tipoEmpresa_idtipoEmpresa', null = True)  # Field name made lowercase.
    provincia_idprovincia = models.ForeignKey(Provincia, models.DO_NOTHING, db_column='provincia_idProvincia', null=True)  # Field name made lowercase.
    ciudad_idciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_idCiudad', null=True)  # Field name made lowercase.
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='Estado_idEstado', null = True) 
    def __str__(self):
        txt = " Ruc/Cédula: {0} / Nombre Comercial: {1} "
        return txt.format(self.ruc_cedula , self.nombrecomercial) 

    def getById(self, idempresa):
        try:
            empresa = Empresa.objects.get(idempresa=idempresa)
            return empresa
        except:
            return None
    
    USERNAME_FIELD='correo'
    REQUIRED_FIELDS=[]

    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresas'
        db_table = 'empresa'

        def __str__(self):
            txt = " Ruc/Cédula: {0} / Nombre Comercial: {1} "
            return  txt.format(self.ruc_cedula , self.nombrecomercial) 
        