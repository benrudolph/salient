# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volume',
            name='docs',
        ),
        migrations.AddField(
            model_name='doc',
            name='text',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc',
            name='text_file',
            field=models.FileField(null=True, upload_to=b'docs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc',
            name='url',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doc',
            name='volume',
            field=models.ForeignKey(default=1, to='uploader.Volume'),
            preserve_default=False,
        ),
    ]
