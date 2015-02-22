# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salient', '0003_worddoc_is_stopword'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='sentiment_neg',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=5, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc',
            name='sentiment_pos',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=5, blank=True),
            preserve_default=True,
        ),
    ]
