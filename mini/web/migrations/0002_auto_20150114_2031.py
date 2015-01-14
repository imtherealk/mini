# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='relationship_status',
            field=models.CharField(max_length=1, null=True, blank=True, choices=[('y', '연애중'), ('n', '싱글'), ('m', '결혼')]),
            preserve_default=True,
        ),
    ]
