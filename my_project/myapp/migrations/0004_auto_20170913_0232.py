# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply',
            name='supply_delete',
            field=models.CharField(choices=[('dele', '已删除'), ('no', '正常')], default='正常', max_length=10, verbose_name='删除状态位'),
        ),
    ]
