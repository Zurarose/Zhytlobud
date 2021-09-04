# Generated by Django 2.2.24 on 2021-09-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20210904_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='construction_phase_prst',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='parking_num',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='quarter',
            field=models.IntegerField(blank=True, db_column='Quarter'),
        ),
        migrations.AlterField(
            model_name='houses',
            name='remark',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='houses',
            name='storeys',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='street_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='houses',
            name='ttl_area_apartments',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='ttl_area_building',
            field=models.FloatField(blank=True),
        ),
    ]
