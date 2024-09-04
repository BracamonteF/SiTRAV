from django.db import models


class Conductores(models.Model):
    documento = models.IntegerField(unique=True)
    tipo_documento = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=100)
    tipo_carnet = models.CharField(max_length=20)
    legajo_vial = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'conductores'
