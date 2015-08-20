# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20150810_1014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='prices',
            options={'ordering': ('price',)},
        ),
    ]
