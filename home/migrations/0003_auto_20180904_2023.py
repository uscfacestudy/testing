# Generated by Django 2.1.1 on 2018-09-04 20:23

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180904_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='prosopagnosia',
            field=models.PositiveSmallIntegerField(choices=[(home.models.PROSOPAGNOSIA(0), 0), (home.models.PROSOPAGNOSIA(1), 1), (home.models.PROSOPAGNOSIA(2), 2)], null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='token',
            field=models.CharField(max_length=24, unique=True),
        ),
    ]