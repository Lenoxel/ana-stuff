# Generated by Django 3.0.4 on 2021-10-06 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_sendmessage_senddate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendmessage',
            options={'ordering': ['sendDate'], 'verbose_name': 'Mensagem', 'verbose_name_plural': 'Mensagens Recebidas'},
        ),
    ]
