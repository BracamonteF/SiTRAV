from django.db import models


class Vehiculos(models.Model):
    patente_nacional = models.CharField(unique=True, max_length=7)
    matrícula_vial = models.CharField(unique=True, max_length=12)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vehiculos'


class Motores(models.Model):
    numero_serie = models.CharField(unique=True, max_length=50)
    matricula_vial = models.CharField(unique=True, max_length=12)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'motores'


class VehiculosMotores(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, models.DO_NOTHING)
    motor = models.ForeignKey(Motores, models.DO_NOTHING)
    fecha_instalacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehiculos_motores'
