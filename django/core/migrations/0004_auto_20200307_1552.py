# Generated by Django 2.1.7 on 2020-03-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200223_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Desconto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='onSale',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Em promoção'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Preço'),
        ),
    ]
