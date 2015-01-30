# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volume',
            name='docs',
        ),
        migrations.DeleteModel(
            name='Doc',
        ),
        migrations.DeleteModel(
            name='Volume',
        ),
    ]
