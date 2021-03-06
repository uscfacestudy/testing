# Generated by Django 2.1 on 2018-08-30 22:48

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=5)),
                ('birthday', models.DateField()),
                ('sex', models.BooleanField()),
                ('prosopagnosia', models.PositiveSmallIntegerField(choices=[(home.models.PROSOPAGNOSIA(0), 0), (home.models.PROSOPAGNOSIA(1), 1), (home.models.PROSOPAGNOSIA(2), 2)])),
            ],
        ),
    ]
