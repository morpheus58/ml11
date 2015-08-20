# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_auto_20150810_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prices',
            options={'ordering': ('price', 'book_type')},
        ),
    ]
