# Generated by Django 2.2.24 on 2021-09-04 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id_areas', models.AutoField(db_column='ID_areas', primary_key=True, serialize=False)),
                ('zone', models.CharField(blank=True, db_column='Zone', max_length=50, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
            ],
            options={
                'db_table': 'areas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('id_buildings', models.AutoField(db_column='ID_buildings', primary_key=True, serialize=False)),
                ('class_field', models.CharField(blank=True, db_column='class', max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('builder', models.CharField(blank=True, max_length=50, null=True)),
                ('urban_develop_zone', models.CharField(blank=True, max_length=50, null=True)),
                ('parking', models.CharField(blank=True, max_length=25, null=True)),
                ('parking_type', models.CharField(blank=True, max_length=25, null=True)),
                ('parking_num', models.IntegerField(blank=True, null=True)),
                ('city_area', models.ForeignKey(blank=True, db_column='city area', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Areas')),
            ],
            options={
                'db_table': 'buildings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Financing',
            fields=[
                ('id_finance', models.AutoField(db_column='ID_finance', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('full_name', models.CharField(blank=True, db_column='Full_name', max_length=50, null=True)),
            ],
            options={
                'db_table': 'financing',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id_house', models.AutoField(db_column='ID_house', primary_key=True, serialize=False)),
                ('street_number', models.CharField(blank=True, max_length=25, null=True)),
                ('ttl_area_building', models.FloatField(blank=True, null=True)),
                ('ttl_area_apartments', models.FloatField(blank=True, null=True)),
                ('storeys', models.IntegerField(blank=True, null=True)),
                ('construction_phase_prst', models.IntegerField(blank=True, null=True)),
                ('parking_num', models.IntegerField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=500, null=True)),
                ('start_year', models.CharField(blank=True, db_column='start_year', max_length=50, null=True)),
                ('commis_year', models.CharField(blank=True, db_column='commis_year', max_length=50, null=True)),
                ('quarter', models.IntegerField(blank=True, db_column='Quarter', null=True)),
                ('id_buildings', models.ForeignKey(blank=True, db_column='ID_buildings', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Buildings')),
            ],
            options={
                'db_table': 'houses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id_log', models.AutoField(db_column='id_log', primary_key=True, serialize=False)),
                ('info', models.CharField(blank=True, db_column='info', max_length=2000, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, db_column='time', null=True)),
            ],
            options={
                'db_table': 'logger',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id_ownership', models.AutoField(db_column='id_ownership', primary_key=True, serialize=False)),
                ('form', models.CharField(blank=True, db_column='form', max_length=50, null=True)),
                ('full_form', models.CharField(blank=True, db_column='full_form', max_length=50, null=True)),
            ],
            options={
                'db_table': 'ownership',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Streets',
            fields=[
                ('id_street', models.AutoField(db_column='ID_street', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'streets',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subways',
            fields=[
                ('id_subway', models.AutoField(db_column='ID_subway', primary_key=True, serialize=False)),
                ('zone', models.CharField(blank=True, db_column='Zone', max_length=50, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
            ],
            options={
                'db_table': 'subways',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id_sections', models.AutoField(db_column='ID_sections', primary_key=True, serialize=False)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('attribute', models.CharField(blank=True, max_length=50, null=True)),
                ('duplex_apartments', models.CharField(blank=True, max_length=50, null=True)),
                ('penthouses', models.CharField(blank=True, max_length=50, null=True)),
                ('apartments_num', models.IntegerField(blank=True, null=True)),
                ('a1_num', models.IntegerField(blank=True, null=True)),
                ('a2_num', models.IntegerField(blank=True, null=True)),
                ('a3_num', models.IntegerField(blank=True, null=True)),
                ('a4_num', models.IntegerField(blank=True, null=True)),
                ('a1_area_min', models.FloatField(blank=True, null=True)),
                ('a1_area_max', models.FloatField(blank=True, null=True)),
                ('a2_area_min', models.FloatField(blank=True, null=True)),
                ('a2_area_max', models.FloatField(blank=True, null=True)),
                ('a3_area_min', models.FloatField(blank=True, null=True)),
                ('a3_area_max', models.FloatField(blank=True, null=True)),
                ('a4_area_min', models.FloatField(blank=True, null=True)),
                ('a4_area_max', models.FloatField(blank=True, null=True)),
                ('avg_area', models.FloatField(blank=True, null=True)),
                ('financing', models.ForeignKey(blank=True, db_column='financing', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Financing')),
                ('id_house', models.ForeignKey(blank=True, db_column='ID_house', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Houses')),
            ],
            options={
                'db_table': 'sections',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SalesAndPrices',
            fields=[
                ('id_row', models.AutoField(db_column='ID_row', primary_key=True, serialize=False)),
                ('parking_price_min', models.FloatField(blank=True, null=True)),
                ('parking_price_max', models.FloatField(blank=True, null=True)),
                ('a1_to_sale', models.IntegerField(blank=True, null=True)),
                ('a1_min_price', models.FloatField(blank=True, null=True)),
                ('a1_max_price', models.FloatField(blank=True, null=True)),
                ('a1_avg_price', models.FloatField(blank=True, null=True)),
                ('a2_to_sale', models.IntegerField(blank=True, null=True)),
                ('a2_min_price', models.FloatField(blank=True, null=True)),
                ('a2_max_price', models.FloatField(blank=True, null=True)),
                ('a2_avg_price', models.FloatField(blank=True, null=True)),
                ('a3_to_sale', models.IntegerField(blank=True, null=True)),
                ('a3_min_price', models.FloatField(blank=True, null=True)),
                ('a3_max_price', models.FloatField(blank=True, null=True)),
                ('a3_avg_price', models.FloatField(blank=True, null=True)),
                ('a4_to_sale', models.IntegerField(blank=True, null=True)),
                ('a4_min_price', models.FloatField(blank=True, null=True)),
                ('a4_max_price', models.FloatField(blank=True, null=True)),
                ('a4_avg_price', models.FloatField(blank=True, null=True)),
                ('a1_area_to_sale', models.FloatField(blank=True, null=True)),
                ('a2_area_to_sale', models.FloatField(blank=True, null=True)),
                ('a3_area_to_sale', models.FloatField(blank=True, null=True)),
                ('a4_area_to_sale', models.FloatField(blank=True, null=True)),
                ('area_remain', models.FloatField(blank=True, null=True)),
                ('dollar', models.FloatField(blank=True, null=True)),
                ('min_price', models.FloatField(blank=True, null=True)),
                ('max_price', models.FloatField(blank=True, null=True)),
                ('avg_price', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('id_sections', models.ForeignKey(blank=True, db_column='ID_sections', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Sections')),
            ],
            options={
                'db_table': 'sales_and_prices',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id_customer', models.AutoField(db_column='ID_customer', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=15, null=True)),
                ('start_work', models.CharField(blank=True, db_column='start_work', max_length=15, null=True)),
                ('ownership', models.ForeignKey(blank=True, db_column='form', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Ownership')),
            ],
            options={
                'db_table': 'customers',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='buildings',
            name='customer',
            field=models.ForeignKey(blank=True, db_column='customer', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Customers'),
        ),
        migrations.AddField(
            model_name='buildings',
            name='street_name',
            field=models.ForeignKey(blank=True, db_column='street_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Streets'),
        ),
        migrations.AddField(
            model_name='buildings',
            name='subway',
            field=models.ForeignKey(blank=True, db_column='subway', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Subways'),
        ),
    ]
