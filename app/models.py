# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Areas(models.Model):
    id_areas = models.AutoField(db_column='ID_areas', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areas'


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


class Buildings(models.Model):
    id_buildings = models.AutoField(db_column='ID_buildings', primary_key=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=50)  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=50)
    street_type = models.CharField(max_length=50)
    street_name = models.ForeignKey('Streets', models.DO_NOTHING, db_column='street_name')
    builder = models.CharField(max_length=50)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customer')
    urban_develop_zone = models.CharField(max_length=50)
    city_area = models.ForeignKey(Areas, models.DO_NOTHING, db_column='city area')  # Field renamed to remove unsuitable characters.
    subway = models.ForeignKey('Subways', models.DO_NOTHING, db_column='subway')
    parking = models.CharField(max_length=25)
    parking_num = models.IntegerField()
    parking_price_hrn = models.FloatField()
    parking_price_dol = models.FloatField()

    class Meta:
        managed = False
        db_table = 'buildings'


class Customers(models.Model):
    id_customer = models.AutoField(db_column='ID_customer', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15)  # Field name made lowercase.
    start_work = models.DateField()

    class Meta:
        managed = False
        db_table = 'customers'


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


class Houses(models.Model):
    id_buildings = models.ForeignKey(Buildings, models.DO_NOTHING, db_column='ID_buildings')  # Field name made lowercase.
    id_house = models.AutoField(db_column='ID_house', primary_key=True)  # Field name made lowercase.
    street_number = models.CharField(max_length=25)
    ttl_area_building = models.FloatField()
    ttl_area_apartments = models.FloatField()
    storeys = models.IntegerField()
    construction_phase_prst = models.IntegerField()
    parking_num = models.IntegerField()
    parking_price_hrn = models.FloatField()
    parking_price_dol = models.FloatField()
    remark = models.CharField(max_length=50)
    commis_year = models.TextField()  # This field type is a guess.
    quarter = models.IntegerField(db_column='Quarter')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'houses'


class SalesAndPrices(models.Model):
    id_row = models.AutoField(db_column='ID_row', primary_key=True)  # Field name made lowercase.
    id_sections = models.ForeignKey('Sections', models.DO_NOTHING, db_column='ID_sections')  # Field name made lowercase.
    a1_min_price = models.FloatField()
    a1_max_price = models.FloatField()
    a1_avg_price = models.FloatField()
    a2_min_price = models.FloatField()
    a2_max_price = models.FloatField()
    a2_avg_price = models.FloatField()
    a3_min_price = models.FloatField()
    a3_max_price = models.FloatField()
    a3_avg_price = models.FloatField()
    a4_min_price = models.FloatField()
    a4_max_price = models.FloatField()
    a4_avg_price = models.FloatField()
    a1_to_sale = models.IntegerField()
    a2_to_sale = models.IntegerField()
    a3_to_sale = models.IntegerField()
    a4_to_sale = models.IntegerField()
    a1_area_to_sale = models.FloatField()
    a2_area_to_sale = models.FloatField()
    a3_area_to_sale = models.FloatField()
    a4_area_to_sale = models.FloatField()
    area_remain = models.FloatField()
    ondate = models.DateField()

    class Meta:
        managed = False
        db_table = 'sales_and_prices'


class Sections(models.Model):
    id_house = models.ForeignKey(Houses, models.DO_NOTHING, db_column='ID_house')  # Field name made lowercase.
    id_sections = models.AutoField(db_column='ID_sections', primary_key=True)  # Field name made lowercase.
    section = models.IntegerField()
    attribute = models.IntegerField()
    financing = models.CharField(max_length=50)
    duplex_apartments = models.IntegerField()
    penthouses = models.IntegerField()
    apartments_num = models.IntegerField()
    a1_num = models.IntegerField()
    a2_num = models.IntegerField()
    a3_num = models.IntegerField()
    a4_num = models.IntegerField()
    a1_area_min = models.FloatField()
    a1_area_max = models.FloatField()
    a2_area_min = models.FloatField()
    a2_area_max = models.FloatField()
    a3_area_min = models.FloatField()
    a3_area_max = models.FloatField()
    a4_area_min = models.FloatField()
    a4_area_max = models.FloatField()
    avg_area = models.FloatField()
    min_price_hrn = models.FloatField()
    max_price_hrn = models.FloatField()
    avg_price_hrn = models.FloatField()
    min_price_dol = models.FloatField()
    max_price_dol = models.FloatField()
    avg_price_dol = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sections'


class Streets(models.Model):
    id_street = models.AutoField(db_column='ID_street', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'streets'


class Subways(models.Model):
    id_subway = models.AutoField(db_column='ID_subway', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subways'
