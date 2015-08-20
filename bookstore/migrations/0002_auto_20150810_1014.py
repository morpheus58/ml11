# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_type', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='books',
            name='price',
        ),
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.ManyToManyField(to='bookstore.Prices'),
        ),
    ]
