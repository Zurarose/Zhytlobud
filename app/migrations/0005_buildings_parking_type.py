# Generated by Django 2.2.24 on 2021-08-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210809_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildings',
            name='parking_type',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]