# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('doc_type', models.CharField(default=b'IN', max_length=2, choices=[(b'UR', b'Web Address'), (b'TX', b'Text Files'), (b'IN', b'User Input')])),
                ('text_file', models.FileField(null=True, upload_to=b'docs', blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('text_hash', models.CharField(max_length=200, null=True, blank=True)),
                ('url', models.CharField(max_length=1000, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WordDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_stemmed', models.CharField(max_length=100, null=True)),
                ('word_raw', models.CharField(max_length=100, null=True)),
                ('position', models.IntegerField(null=True)),
                ('doc', models.ForeignKey(blank=True, to='salient.Doc', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='doc',
            name='volumes',
            field=models.ManyToManyField(to='salient.Volume', null=True, blank=True),
            preserve_default=True,
        ),
    ]
