# Generated by Django 3.2.6 on 2021-09-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_dci_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Forme',
            field=models.CharField(max_length=100, null=True, verbose_name='Forme '),
        ),
        migrations.AlterField(
            model_name='product',
            name='Spécification',
            field=models.CharField(max_length=100, null=True, verbose_name='Spécification '),
        ),
    ]