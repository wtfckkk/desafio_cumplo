from django.db import models


class TipoConsulta(models.Model):
        nombre = models.CharField(max_length=60)

        def __str__(self):
            return '{}' .format(self.nombre)

class Consulta(models.Model):
        fecha_inicio = models.DateField()
        fecha_fin = models.DateField()
        tipo_consulta = models.ForeignKey(TipoConsulta, null=False, blank=False, on_delete=models.PROTECT)
        created = models.DateTimeField(auto_now_add=True)
