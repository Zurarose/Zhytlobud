# Generated by Django 2.2.24 on 2021-10-08 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_subways_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildings',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
