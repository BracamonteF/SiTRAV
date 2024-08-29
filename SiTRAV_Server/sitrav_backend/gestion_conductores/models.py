# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
