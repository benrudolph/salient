# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_auto_20150202_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='volume',
        ),
        migrations.AddField(
            model_name='doc',
            name='volumes',
            field=models.ManyToManyField(to='uploader.Volume', null=True),
            preserve_default=True,
        ),
    ]
