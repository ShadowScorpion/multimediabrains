# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=30)),
                ('id_pk', models.IntegerField(default=0)),
                ('scores', models.IntegerField(default=0)),
                ('photo', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(verbose_name='date')),
            ],
        ),
        migrations.DeleteModel(
            name='Registraion',
        ),
    ]