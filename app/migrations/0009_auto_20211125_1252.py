# Generated by Django 3.2.8 on 2021-11-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_additionally_finance_land_outdoor_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='storeys',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sections',
            name='number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
