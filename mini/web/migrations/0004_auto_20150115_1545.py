# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20150114_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, max_length=11, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='C:\\Users\\my\\Development\\Projects\\mini\\mini\\media\\sandbox\\post-images', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='sandbox/profile-images', null=True),
            preserve_default=True,
        ),
    ]
