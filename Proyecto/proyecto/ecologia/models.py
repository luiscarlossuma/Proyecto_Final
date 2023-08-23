from django.db import models
from django.utils import timezone

class Reportes(models.Model):

    class Meta:
        verbose_name = "Reportes"
        verbose_name_plural = "Reportes"

    fec_rep = models.DateTimeField('Fecha del reporte', default=timezone.now)
    asunto = models.CharField('Asunto del reporte', max_length=300, blank=False, default = 'Asunto del reporte')
    detalles = models.TextField('Detalles del reporte', blank=False, default = 'Describe tu reporte tan detallado como sea posible')

    def _str_(self):
        return self.asunto