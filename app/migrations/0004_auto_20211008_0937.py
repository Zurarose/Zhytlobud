# Generated by Django 2.2.24 on 2021-10-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_buildings_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildings',
            name='url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
