# Generated by Django 3.0.4 on 2021-10-06 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200406_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=120, verbose_name='Nome')),
                ('comment', models.TextField(max_length=600, verbose_name='Comentário')),
                ('sentOn', models.DateTimeField(auto_now_add=True, verbose_name='Enviado em')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='comment',
            field=models.TextField(max_length=300, verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='evaluator_name',
            field=models.CharField(max_length=80, verbose_name='Avaliador'),
        ),
    ]
