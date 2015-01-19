# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20150115_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(upload_to='sandbox/profile-images', null=True, default='sandbox/profile-images/default_profile.png', blank=True),
            preserve_default=True,
        ),
    ]
