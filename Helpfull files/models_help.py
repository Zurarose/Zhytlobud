"""
Definition of models.
"""
# Create your models here.
from django.db import models

class Materials(models.Model):
    id_material = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=75, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=75, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=75, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=75, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'materials'

class OrderedMaterial(models.Model):
    id_order = models.ForeignKey('Orders', on_delete=models.CASCADE, db_column='id_order')
    id_material = models.ForeignKey(Materials, on_delete=models.CASCADE, db_column='id_material', blank=True, null=True)
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ordered_material'

class Orders(models.Model):
    id_order = models.AutoField(primary_key=True)
    date_order = models.DateField(blank=True, null=True)
    date_complete = models.DateField(blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=75, blank=True, null=True)

    class Meta:
        db_table = 'orders'


class UsedMaterial(models.Model):
    id_order = models.ForeignKey('BuildOrders', on_delete=models.CASCADE, db_column='id_order')
    id_material = models.ForeignKey(Materials, on_delete=models.CASCADE, db_column='id_material', blank=True, null=True)
    count = models.IntegerField(db_column='Count', blank=True, null=True)
    price = models.FloatField(db_column='Price', blank=True, null=True)
   

    class Meta:
        db_table = 'used_material'

class BuildOrders(models.Model):
    id_order = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=75, blank=True, null=True)
    desc = models.CharField(db_column='Description', max_length=150, blank=True, null=True)
    date_order = models.DateField(blank=True, null=True)
    date_complete = models.DateField(blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=75, blank=True, null=True)
    scost = models.FloatField(db_column='Service costs', blank=True, null=True)
    ocost = models.FloatField(db_column='Other costs', blank=True, null=True)

    class Meta:
        db_table = 'build_orders'

