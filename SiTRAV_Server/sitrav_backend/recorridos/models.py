# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Recorridos(models.Model):
    conductor = models.ForeignKey('gestion_conductores.Conductores', models.DO_NOTHING)
    vehiculo = models.ForeignKey('gestion_vehiculos.Vehiculos', models.DO_NOTHING)

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
