# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('todo', models.CharField(max_length=255)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]