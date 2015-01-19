# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20150119_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='post-images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='/profile-images/default_profile.png', blank=True, upload_to='profile-images'),
            preserve_default=True,
        ),
    ]
