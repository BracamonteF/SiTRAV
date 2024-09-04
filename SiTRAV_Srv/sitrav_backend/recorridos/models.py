from django.db import models


class Recorridos(models.Model):
    conductor = models.ForeignKey('gestor_conductores.Conductores', models.DO_NOTHING)
    vehiculo = models.ForeignKey('gestor_vehiculos.Vehiculos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recorridos'


class Posiciones(models.Model):
    recorrido = models.ForeignKey(Recorridos, models.DO_NOTHING)
    latitud = models.DecimalField(max_digits=10, decimal_places=7)
    longitud = models.DecimalField(max_digits=10, decimal_places=7)
    fecha_hora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'posiciones'