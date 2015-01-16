# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20150115_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='sandbox/profile-images/default.png', upload_to='sandbox/profile-images', blank=True),
            preserve_default=True,
        ),
    ]
