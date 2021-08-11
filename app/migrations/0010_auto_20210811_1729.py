# Generated by Django 2.2.24 on 2021-08-11 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210810_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildings',
            name='city_area',
            field=models.ForeignKey(blank=True, db_column='city area', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Areas'),
        ),
        migrations.AlterField(
            model_name='buildings',
            name='customer',
            field=models.ForeignKey(blank=True, db_column='customer', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Customers'),
        ),
        migrations.AlterField(
            model_name='buildings',
            name='street_name',
            field=models.ForeignKey(blank=True, db_column='street_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Streets'),
        ),
        migrations.AlterField(
            model_name='buildings',
            name='subway',
            field=models.ForeignKey(blank=True, db_column='subway', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Subways'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='ownership',
            field=models.ForeignKey(blank=True, db_column='form', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Ownership'),
        ),
        migrations.AlterField(
            model_name='houses',
            name='id_buildings',
            field=models.ForeignKey(blank=True, db_column='ID_buildings', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Buildings'),
        ),
        migrations.AlterField(
            model_name='salesandprices',
            name='id_sections',
            field=models.ForeignKey(blank=True, db_column='ID_sections', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Sections'),
        ),
        migrations.AlterField(
            model_name='sections',
            name='financing',
            field=models.ForeignKey(blank=True, db_column='financing', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Financing'),
        ),
        migrations.AlterField(
            model_name='sections',
            name='id_house',
            field=models.ForeignKey(blank=True, db_column='ID_house', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Houses'),
        ),
    ]
