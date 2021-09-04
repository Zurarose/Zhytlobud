# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime

class Logger(models.Model):
    id_log = models.AutoField(db_column='id_log', primary_key=True)  # Field name made lowercase.
    info = models.CharField(db_column='info', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='time',auto_now_add=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'logger'

class Areas(models.Model):
    id_areas = models.AutoField(db_column='ID_areas', primary_key=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'areas'

class Streets(models.Model):
    id_street = models.AutoField(db_column='ID_street', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'streets'


class Subways(models.Model):
    id_subway = models.AutoField(db_column='ID_subway', primary_key=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'subways'

class Ownership(models.Model):
    id_ownership = models.AutoField(db_column='id_ownership', primary_key=True)  # Field name made lowercase.
    form = models.CharField(db_column='form', max_length=50, blank=True, null=True)  # Field name made lowercase.
    full_form = models.CharField(db_column='full_form', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ownership'

class Customers(models.Model):
    id_customer = models.AutoField(db_column='ID_customer', primary_key=True)  # Field name made lowercase.
    ownership = models.ForeignKey(Ownership, models.SET_NULL, db_column='form', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    start_work = models.CharField(db_column='start_work', max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customers'

class Buildings(models.Model):
    id_buildings = models.AutoField(db_column='ID_buildings', primary_key=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=50)
    street_name = models.ForeignKey(Streets, models.SET_NULL, db_column='street_name', blank=True, null=True)
    builder = models.CharField(max_length=50, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.SET_NULL, db_column='customer', blank=True, null=True)
    urban_develop_zone = models.CharField(max_length=50, blank=True, null=True)
    city_area = models.ForeignKey(Areas, models.SET_NULL, db_column='city area', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    subway = models.ForeignKey(Subways, models.SET_NULL, db_column='subway', blank=True, null=True)
    parking = models.CharField(max_length=25, blank=True, null=True)
    parking_type = models.CharField(max_length=25, blank=True, null=True)
    parking_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'buildings'

class Financing(models.Model):
    id_finance = models.AutoField(db_column='ID_finance', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'financing'



class Houses(models.Model):
    id_buildings = models.ForeignKey(Buildings, models.CASCADE, db_column='ID_buildings', blank=True, null=True)  # Field name made lowercase.
    id_house = models.AutoField(db_column='ID_house', primary_key=True)  # Field name made lowercase.
    street_number = models.CharField(max_length=25, blank=True, null=True)
    ttl_area_building = models.FloatField(blank=True, null=True)
    ttl_area_apartments = models.FloatField(blank=True, null=True)
    storeys = models.IntegerField(blank=True, null=True)
    construction_phase_prst = models.IntegerField(blank=True, null=True)
    parking_num = models.IntegerField(blank=True, null=True)   
    remark = models.CharField(max_length=500, blank=True, null=True)
    start_year = models.CharField(db_column='start_year', max_length=50, blank=True, null=True)  # This field type is a guess.
    commis_year = models.CharField(db_column='commis_year', max_length=50, blank=True, null=True)  # This field type is a guess.
    quarter = models.IntegerField(db_column='Quarter', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'houses'

class SalesAndPrices(models.Model):
    id_row = models.AutoField(db_column='ID_row', primary_key=True)  # Field name made lowercase.
    id_sections = models.ForeignKey('Sections', models.CASCADE, db_column='ID_sections', blank=True, null=True)  # Field name made lowercase.
    parking_price_min = models.FloatField(blank=True, null=True)
    parking_price_max = models.FloatField(blank=True, null=True)
    a1_to_sale = models.IntegerField(blank=True, null=True)
    a1_min_price = models.FloatField(blank=True, null=True)
    a1_max_price = models.FloatField(blank=True, null=True)
    a1_avg_price = models.FloatField(blank=True, null=True)
    a2_to_sale = models.IntegerField(blank=True, null=True)
    a2_min_price = models.FloatField(blank=True, null=True)
    a2_max_price = models.FloatField(blank=True, null=True)
    a2_avg_price = models.FloatField(blank=True, null=True)
    a3_to_sale = models.IntegerField(blank=True, null=True)
    a3_min_price = models.FloatField(blank=True, null=True)
    a3_max_price = models.FloatField(blank=True, null=True)
    a3_avg_price = models.FloatField(blank=True, null=True)
    a4_to_sale = models.IntegerField(blank=True, null=True)
    a4_min_price = models.FloatField(blank=True, null=True)
    a4_max_price = models.FloatField(blank=True, null=True)
    a4_avg_price = models.FloatField(blank=True, null=True)
    a1_area_to_sale = models.FloatField(blank=True, null=True)
    a2_area_to_sale = models.FloatField(blank=True, null=True)
    a3_area_to_sale = models.FloatField(blank=True, null=True)
    a4_area_to_sale = models.FloatField(blank=True, null=True)
    area_remain = models.FloatField(blank=True, null=True)
    dollar = models.FloatField(blank=True, null=True)
    min_price = models.FloatField(blank=True, null=True)
    max_price = models.FloatField(blank=True, null=True)
    avg_price = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sales_and_prices'


class Sections(models.Model):
    id_house = models.ForeignKey(Houses, models.CASCADE, db_column='ID_house', blank=True, null=True)  # Field name made lowercase.
    id_sections = models.AutoField(db_column='ID_sections', primary_key=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    financing = models.ForeignKey(Financing, models.CASCADE, db_column='financing', blank=True, null=True)
    duplex_apartments = models.CharField(max_length=50, blank=True, null=True)
    penthouses = models.CharField(max_length=50, blank=True, null=True)
    apartments_num = models.IntegerField(blank=True, null=True)
    a1_num = models.IntegerField(blank=True, null=True)
    a2_num = models.IntegerField(blank=True, null=True)
    a3_num = models.IntegerField(blank=True, null=True)
    a4_num = models.IntegerField(blank=True, null=True)
    a1_area_min = models.FloatField(blank=True, null=True)
    a1_area_max = models.FloatField(blank=True, null=True)
    a2_area_min = models.FloatField(blank=True, null=True)
    a2_area_max = models.FloatField(blank=True, null=True)
    a3_area_min = models.FloatField(blank=True, null=True)
    a3_area_max = models.FloatField(blank=True, null=True)
    a4_area_min = models.FloatField(blank=True, null=True)
    a4_area_max = models.FloatField(blank=True, null=True)
    avg_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sections'



#Django tables
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


