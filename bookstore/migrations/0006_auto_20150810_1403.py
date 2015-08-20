# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20150810_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prices',
            options={'ordering': ('book_type',)},
        ),
    ]
