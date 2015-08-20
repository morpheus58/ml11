# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20150810_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='summary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='prices',
            name='price',
            field=models.FloatField(),
        ),
    ]
