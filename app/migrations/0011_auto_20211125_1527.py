# Generated by Django 3.2.8 on 2021-11-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20211125_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildings',
            name='Render',
            field=models.ImageField(default=None, upload_to='imgs'),
        ),
        migrations.AlterField(
            model_name='buildings',
            name='map',
            field=models.ImageField(default=None, upload_to='imgs'),
        ),
    ]