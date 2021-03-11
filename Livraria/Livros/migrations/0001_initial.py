# Generated by Django 3.1.7 on 2021-03-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('autor', models.CharField(max_length=30, unique=True)),
                ('qtd_paginas', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('data_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
