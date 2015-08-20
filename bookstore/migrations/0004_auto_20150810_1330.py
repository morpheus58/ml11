# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20150810_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='author',
            new_name='authors',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='price',
            new_name='prices',
        ),
    ]
