# Generated by Django 2.1.7 on 2020-04-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200406_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='evaluation',
            field=models.PositiveSmallIntegerField(verbose_name='Avaliação'),
        ),
    ]
