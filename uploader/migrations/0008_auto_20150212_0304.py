# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0007_doc_text_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='user',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='volumes',
        ),
        migrations.RemoveField(
            model_name='volume',
            name='user',
        ),
        migrations.DeleteModel(
            name='Volume',
        ),
        migrations.RemoveField(
            model_name='worddoc',
            name='doc',
        ),
        migrations.DeleteModel(
            name='Doc',
        ),
        migrations.DeleteModel(
            name='WordDoc',
        ),
    ]
