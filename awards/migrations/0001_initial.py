# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-31 12:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(default='photos/default.jpg', upload_to='photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('contact', models.CharField(max_length=12)),
            ],
        ),
    ]
