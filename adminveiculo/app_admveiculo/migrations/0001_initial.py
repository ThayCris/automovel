# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaDeVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(help_text='Ex. Nissan, Renault, Chevrolet, Fiat', max_length=20, verbose_name='Marca do Veiculo')),
            ],
            options={
                'verbose_name': 'Marca do Veículo',
                'verbose_name_plural': 'Marcas dos Veículos',
                'ordering': ('marca',),
            },
        ),
        migrations.CreateModel(
            name='TipoDeVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(help_text='Ex: Carro, Moto ou Caminhão', max_length=20, verbose_name='Tipo de Veículo')),
            ],
            options={
                'verbose_name': 'Tipo de Veículo',
                'verbose_name_plural': 'Tipos de Veículos',
                'ordering': ('tipo',),
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=75, verbose_name='Modelo')),
                ('placa', models.CharField(max_length=75, verbose_name='Placa')),
                ('cor', models.CharField(max_length=75, verbose_name='Cor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admveiculo.MarcaDeVeiculo')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admveiculo.TipoDeVeiculo')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
                'ordering': ('tipo', 'marca', 'modelo'),
            },
        ),
    ]
