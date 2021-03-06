# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição')),
                ('publication_date', models.DateField(verbose_name='Data de Publicação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
                ('published', models.BooleanField()),
                ('file', models.FileField(upload_to='upload/file', verbose_name='Arquivo')),
            ],
        ),
    ]
