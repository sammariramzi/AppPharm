# Generated by Django 3.2.6 on 2021-09-13 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_vente_added_vente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe_thérapeutique',
            name='Nom_thérapeutique',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Classe Thérapeutique '),
        ),
        migrations.AlterField(
            model_name='dci',
            name='Nom',
            field=models.TextField(max_length=50, primary_key=True, serialize=False, verbose_name='DCI '),
        ),
        migrations.AlterField(
            model_name='echange',
            name='Qte',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantité '),
        ),
        migrations.AlterField(
            model_name='laboratoire',
            name='Adresse',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pharmaci',
            name='Adresse',
            field=models.CharField(max_length=100, null=True, verbose_name='Adresse '),
        ),
        migrations.AlterField(
            model_name='pharmaci',
            name='Nom_Ph',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Pharmaci '),
        ),
        migrations.AlterField(
            model_name='product',
            name='Qte',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantité '),
        ),
        migrations.AlterField(
            model_name='sous_classe',
            name='Nom_classe',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Sous Classe '),
        ),
        migrations.AlterField(
            model_name='vente',
            name='Qte',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantité'),
        ),
    ]
