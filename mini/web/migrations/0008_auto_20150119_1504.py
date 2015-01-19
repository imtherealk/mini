# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20150116_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='/post-images', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='/profile-images/default.png', upload_to='/profile-images', blank=True),
            preserve_default=True,
        ),
    ]
