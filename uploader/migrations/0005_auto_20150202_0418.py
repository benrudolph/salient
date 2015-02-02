# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0004_auto_20150202_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='volumes',
            field=models.ManyToManyField(to=b'uploader.Volume', null=True, blank=True),
        ),
    ]
