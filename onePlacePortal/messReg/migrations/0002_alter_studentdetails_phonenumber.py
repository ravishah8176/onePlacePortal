# Generated by Django 4.1.1 on 2022-09-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messReg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='phoneNumber',
            field=models.IntegerField(),
        ),
    ]
