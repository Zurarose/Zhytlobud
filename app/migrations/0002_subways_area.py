# Generated by Django 2.2.24 on 2021-09-28 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subways',
            name='area',
            field=models.ForeignKey(blank=True, db_column='id_areas', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Areas'),
        ),
    ]
