# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20150126_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='accepted',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
