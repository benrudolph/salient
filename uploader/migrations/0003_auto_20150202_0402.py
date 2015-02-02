# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20150130_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='doc',
            name='text_file',
            field=models.FileField(null=True, upload_to=b'docs', blank=True),
        ),
        migrations.AlterField(
            model_name='doc',
            name='url',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='doc',
            name='volume',
            field=models.ForeignKey(to='uploader.Volume', null=True),
        ),
    ]
