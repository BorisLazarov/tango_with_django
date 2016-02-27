# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20160227_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=144)),
                ('author', models.ForeignKey(to='rango.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.FloatField(),
        ),
    ]
