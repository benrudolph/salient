# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0005_auto_20150202_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_stemmed', models.CharField(max_length=100, null=True)),
                ('word_raw', models.CharField(max_length=100, null=True)),
                ('position', models.IntegerField(null=True)),
                ('doc', models.ForeignKey(blank=True, to='uploader.Doc', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
