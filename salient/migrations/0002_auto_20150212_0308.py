# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='volumes',
            field=models.ManyToManyField(to=b'salient.Volume', blank=True),
        ),
    ]
