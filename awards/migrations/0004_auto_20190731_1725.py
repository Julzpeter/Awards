# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-31 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]