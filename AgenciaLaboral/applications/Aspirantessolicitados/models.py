from django.db import models

# Create your models here.
from applications.Solicitud.models import Solicitud
from applications.Estado.models import Estado
from applications.Aspirante.models import Aspirante

class Aspirantessolicitados(models.Model):
    idaspirantessolicitados = models.AutoField(db_column='idAspirantesSolicitados', primary_key=True)  # Field name made lowercase.
    fechaaceptacion = models.DateTimeField(db_column='fechaAceptacion', blank=True, null=True)  # Field name made lowercase.
    solicitud_idsolicitud = models.ForeignKey(Solicitud, models.DO_NOTHING, db_column='Solicitud_idSolicitud')  # Field name made lowercase.
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='Estado_idEstado')  # Field name made lowercase.
    aspirante_idaspirante = models.ForeignKey(Aspirante, models.DO_NOTHING, db_column='Aspirante_idaspirante' , null = True)  # Field name made lowercase.
    
    def __str__(self):
        txt = " fechaaceptacion: {0} / solicitud_idsolicitud: {1} / aspirante_idaspirante: {2} "
        return txt.format(self.fechaaceptacion , self.solicitud_idsolicitud , self.aspirante_idaspirante ) 

    class Meta:
        
        db_table = 'aspirantessolicitados'
        unique_together = (('idaspirantessolicitados', 'estado_idestado'),)