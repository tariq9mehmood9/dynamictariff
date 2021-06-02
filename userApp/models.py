# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class TblBusdata(models.Model):
#     busno = models.IntegerField(db_column='busNo', primary_key=True)  # Field name made lowercase.
#     buscode = models.IntegerField(db_column='busCode')  # Field name made lowercase.
#     busname = models.CharField(db_column='busName', max_length=50)  # Field name made lowercase.
#     voltage = models.FloatField()
#     angle = models.FloatField()
#     loadmw = models.FloatField(db_column='loadMW')  # Field name made lowercase.
#     loadmvar = models.FloatField(db_column='loadMVar')  # Field name made lowercase.
#     genmw = models.FloatField(db_column='genMW')  # Field name made lowercase.
#     genmvar = models.FloatField(db_column='genMVar')  # Field name made lowercase.
#     genqmin = models.FloatField(db_column='genQmin')  # Field name made lowercase.
#     genqmax = models.FloatField(db_column='genQmax')  # Field name made lowercase.
#     injmvar = models.FloatField(db_column='injMVar')  # Field name made lowercase.

#     class Meta:
#         db_table = 'tbl_busdata'


# class TblCost(models.Model):
#     alpha = models.FloatField(blank=True, null=True)
#     beta = models.FloatField(blank=True, null=True)
#     gamma = models.FloatField(blank=True, null=True)

#     class Meta:
#         db_table = 'tbl_cost'


# class TblLinedata(models.Model):
#     frombus = models.IntegerField(db_column='fromBus')  # Field name made lowercase.
#     tobus = models.IntegerField(db_column='toBus')  # Field name made lowercase.
#     resistance = models.FloatField()
#     reactance = models.FloatField()
#     capacitance = models.FloatField()
#     transratio = models.FloatField(db_column='transRatio')  # Field name made lowercase.

#     class Meta:
#         db_table = 'tbl_linedata'


# class TblMwlimits(models.Model):
#     pmin = models.FloatField(db_column='Pmin', blank=True, null=True)  # Field name made lowercase.
#     pmax = models.FloatField(db_column='Pmax', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tbl_mwlimits'


# class TblUnitprice(models.Model):
#     hour = models.IntegerField()
#     cost = models.FloatField()

#     class Meta:
#         db_table = 'tbl_unitprice'
